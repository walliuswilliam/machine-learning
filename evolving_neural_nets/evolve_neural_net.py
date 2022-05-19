import random, math, numpy as np, copy

class Neuron:
    def __init__(self, index, actv_func, is_bias=False):
        self.parents = []
        self.children = []
        self.index = index
        self.bias = is_bias
        self.input = None
        self.gradient = 0
        self.actv_func = actv_func
        if is_bias:
            self.output = 1
        else:
            self.output = None
    

class NeuralNet:
    def __init__(self, weights, data, actv_func, num_neurons, bias_nodes, alpha=0.5, neurons=False):
        self.weights = weights
        self.actv_func = actv_func
        self.biases = bias_nodes
        if neurons:
            self.neurons = neurons
        else:
            self.neurons = [Neuron(i,self.actv_func) if i not in self.biases else Neuron(i,self.actv_func,is_bias=True) for i in range(1,num_neurons+1)]
        self.root_neuron = None
        self.data = data
        if not neurons:
            self.set_node_relations()
        self.alpha = alpha #mutation rate
    
    def get_neuron(self, neuron_index):
        for neuron in self.neurons:
            if neuron.index == neuron_index:
                return neuron

    def set_node_relations(self):
        for nodes in self.weights.keys():
            neuron = self.get_neuron(nodes[0])
            neuron.children.append(self.get_neuron(nodes[1]))

            neuron = self.get_neuron(nodes[1])
            neuron.parents.append(self.get_neuron(nodes[0]))
    
    def set_neuron_output(self, neuron):
        neuron.output = neuron.actv_func(neuron.input)
    
    def change_neuron_actv_func(self, neuron_index, f):
        neuron = self.get_neuron(neuron_index)
        neuron.actv_func = f

    def clear_net(self):
        for neuron in self.neurons:
            if not neuron.bias:
                neuron.input = None
                neuron.output = None

    def forward_propagate(self, initial_input):
        self.clear_net()
        for neuron in self.neurons:
            if len(neuron.parents) == 0 and neuron.bias == False:
                self.root_neuron = neuron
        self.root_neuron.input = initial_input

        queue = [self.root_neuron]
        visited = []
        while queue != []:
            curr_neuron = queue[0]
            if curr_neuron != self.root_neuron and neuron.bias == False:
                curr_neuron.input = self.calc_neuron_input(curr_neuron)
            self.set_neuron_output(curr_neuron)
            visited.append(curr_neuron)
            for child in curr_neuron.children:
                if child not in visited:
                    queue.append(child)
            queue.pop(0)

    def predict(self, initial_input):
        self.forward_propagate(initial_input)
        return self.neurons[-1].output
        
    def print_network(self):
        for neuron in self.neurons:
            if neuron.bias:
                print(f'neuron {neuron.index} (Bias)\ninput: {neuron.input}\noutput: {neuron.output}\n')
            else:
                print(f'neuron {neuron.index}\ninput: {neuron.input}\noutput: {neuron.output}\n')
    
    def get_weight(self, neuron1, neuron2):
        for node_pair in self.weights.keys():
            if set(node_pair) == {neuron1.index, neuron2.index}:
                return self.weights[node_pair]

    def calc_neuron_input(self, neuron):
        total = 0
        for weight_nodes in self.weights.keys():
            if weight_nodes[1] == neuron.index:
                parent = self.get_neuron(weight_nodes[0])
                total += self.weights[weight_nodes]*parent.output
        return total

    def rss(self):
        rss = 0
        for point in self.data:
            output = self.predict(point[0])
            rss += (output - point[1])**2
        return rss

    @classmethod
    def create_random_nn(cls, node_layer_sizes, data, actv_func):
        weights = {}
        biases = []
        current_node_num = 0
        layers = []
        for layer_idx, layer_size in enumerate(node_layer_sizes):
            current_layer = []
            if layer_idx != 0 and layer_idx != len(node_layer_sizes)-1:
                layer_size += 1
            for i in range(layer_size):
                current_node_num += 1
                current_layer.append(current_node_num) 
                if i+1 == layer_size and layer_idx != 0 and layer_idx != len(node_layer_sizes)-1:
                    biases.append(current_node_num)
            layers.append(current_layer)

        for layer_idx, layer in enumerate(layers):
            try:
                next_layer = layers[layer_idx+1]
            except:
                continue
            links = cls.link_layers(layer, next_layer, biases)
            for link in links:
                weights[link] = random.uniform(-0.2,0.2)
        return cls(weights, data, actv_func, layers[-1][-1], biases)
    @classmethod
    def link_layers(cls, layer1, layer2, biases):
        links = []
        for parent in layer1:
            for child in layer2:
                if child not in biases:
                    links.append((parent, child))
        return links

        
def create_initial_generation(node_layer_sizes, data, actv_func):
  return [NeuralNet.create_random_nn(node_layer_sizes, data, actv_func) for _ in range(30)]

def create_new_generation(gen):
  sorted_rss = sorted(gen, key=lambda x: x.rss())[:15]
  new_gen = sorted_rss.copy()

  for parent in sorted_rss:
    child_weights = {}
    for pair, weight in parent.weights.items():
      child_weights[pair] = weight+parent.alpha*np.random.normal()
    child_mut_rate = parent.alpha*(math.exp(np.random.normal()/(2**(1/2)*(len(parent.weights))**(1/4))))
    child = NeuralNet(child_weights, parent.data, parent.actv_func, len(parent.neurons), parent.biases, alpha=child_mut_rate, neurons=parent.neurons)
    print(child.biases)
    new_gen.append(child)
  
  return new_gen

def get_avg_rss(gen):
    rss = [net.rss() for net in gen]
    return sum(rss)/len(rss)
