import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, index, is_bias=False):
        self.parents = []
        self.index = index
        self.bias = is_bias
        self.input = None
        self.gradient = 0
        if is_bias:
            self.children = []
            self.output = 1
        else:
            self.children = []
            self.output = None
    
    def actv_func(self,neuron_input):
        return max(0,neuron_input)
    
    def set_output(self, neuron_input):
        self.output = self.actv_func(neuron_input)


class NeuralNet:
    def __init__(self, weights, data):
        self.weights = weights
        self.biases = [2,5]
        self.neurons = [Neuron(i) if i not in self.biases else Neuron(i, is_bias=True) for i in range(1,7)]
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
            curr_neuron.set_output(curr_neuron.input)
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




data = {(0,5),(2,3),(5,10)}
neuron_weights = {(1,3):1, (1,4):1, (2,3):1, (2,4):1, (3,6):1, (4,6):1, (5,6):1}

net = NeuralNet(neuron_weights, data)

f_prime = lambda x: 0 if x<=0 else 1

net.gradient_descent(2, f_prime)


inputs = [i/100 for i in range(800)]
outputs = [net.predict(i/100) for i in range(800)]


plt.clf()
plt.style.use('bmh')
plt.title("Neural Network Regression")
plt.scatter([0,2,5],[5,3,10], label='Datapoints')
plt.plot(inputs, outputs, label="Initial Regression")




RSS_vals = net.gradient_descent(2000, f_prime, return_rss=True)
print(net.weights)

outputs = [net.predict(i/100) for i in range(800)]

plt.plot(inputs, outputs, label="Final Regression")
plt.xlabel('Inputs')
plt.ylabel('Outputs')
plt.legend()

plt.savefig('analysis/net_backprop_output.png')

plt.clf()
plt.title("Neural Network RSS")
plt.plot([100*i for i in range(20)], RSS_vals)
plt.xlabel('Number of Iterations')
plt.ylabel('RSS')
plt.savefig('analysis/net_backprop_RSS.png')