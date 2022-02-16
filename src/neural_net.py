class Neuron:
    def __init__(self, index, is_bias=False):
        self.parents = []
        self.children = []
        self.index = index
        self.bias = is_bias
        self.input = None
        self.gradient = 0
        if is_bias:
            self.output = 1
        else:
            self.output = None
    

class NeuralNet:
    def __init__(self, weights, data, actv_func, num_neurons, bias_nodes):
        self.weights = weights
        self.actv_func = actv_func
        self.biases = bias_nodes
        self.neurons = [Neuron(i) if i not in self.biases else Neuron(i, is_bias=True) for i in range(1,num_neurons+1)]
        self.root_neuron = None
        self.data = data
        self.set_node_relations()
    
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
        neuron.output = self.actv_func(neuron.input)

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
    
    def set_neuron_gradients(self, point, f_prime):
        self.forward_propagate(point[0])
        neurons = self.neurons.copy()
        neurons.sort(reverse=True, key=lambda x:x.index)

        for neuron in neurons:
            if neuron.index == len(neurons):
                neuron.gradient = 2*(neuron.output-point[1])
            else:
                for child in neuron.children:
                    edge_weight = self.get_weight(child, neuron)
                    neuron.gradient = child.gradient*f_prime(child.input)*edge_weight #maybe add to val??

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

    def calc_weight_gradients(self, f_prime):
        gradients = {key:0 for key in self.weights.keys()}
        for node_pair in self.weights.keys():
            for point in self.data:
                self.set_neuron_gradients(point, f_prime)
                neurons = [self.get_neuron(x) for x in node_pair]
                gradients[node_pair] += neurons[1].gradient*f_prime(neurons[1].input)*neurons[0].output
        return gradients
    
    def f_prime(self, input):
        delta = 0.000000001
        return (self.f(input+delta/2) - self.f(input-delta/2))/delta

    def rss(self):
        rss = 0
        for point in self.data:
            output = self.predict(point[0])
            rss += (output - point[1])**2
        return rss
    
    def gradient_descent(self, num_iterations, f_prime, alpha=0.0001, return_rss=False):
        RSS_vals = []
        for i in range(num_iterations):
            gradients = self.calc_weight_gradients(f_prime)
            self.weights = {key:self.weights[key] - alpha*gradients[key] for key in self.weights}
            if i%100 == 0:
                RSS_vals.append(self.rss())
        if return_rss:
            return RSS_vals
