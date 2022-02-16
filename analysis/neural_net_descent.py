import matplotlib.pyplot as plt

data = {(0,5),(2,3),(5,10)}
neuron_weights = {(1,3):1, (1,4):1, (2,3):1, (2,4):1, (3,6):1, (4,6):1, (5,6):1}

def actv_func(i):
    return max(0,i)

def predict(x, weights):
    return actv_func(weights[(3,6)]*actv_func(weights[(1,3)]*actv_func(x)+weights[(2,3)])+weights[(4,6)]*actv_func(weights[(1,4)]*actv_func(x)+weights[(2,4)])+weights[(5,6)])

def rss(weights):
    total = 0
    for point in data:
        y_act = point[1]
        y_pred = predict(point[0], weights)
        total += (y_act-y_pred)**2
    return total

x = [0.1*x for x in range(200)]
y = [predict(num,neuron_weights) for num in x]


plt.clf()
plt.style.use('bmh')
plt.title("Neural Net Regression Modeling")
plt.scatter([0,2,5],[5,3,10], label='Datapoints')
plt.plot(x, y, label="Initial Regression")


def compute_gradient(weights, delta=0.001):
    gradient = {}
    for edge in weights:
        partial = 0
        temp_point = weights.copy()
        temp_point[edge] += delta/2
        partial += rss(temp_point)
        temp_point[edge] -= delta
        partial -= rss(temp_point)
        gradient[edge] = partial/delta

    return gradient
    
    
    # gradient = {}
    # for weight in weights:
    #     weight_dict_add = {key:value+0.5*delta for key, value in weights.copy().items()}
    #     weight_dict_sub = {key:value-0.5*delta for key, value in weights.copy().items()}
    #     deriv = (rss(weight_dict_add)-rss(weight_dict_sub))/delta
    #     gradient[weight] = deriv
    # return gradient

def descend(weights, num_iterations, delta=0.001, alpha=0.01):
    copy_weights = weights.copy()
    print(f'initial')
    print('rss:', rss(copy_weights))
    print('weights:', copy_weights)
    for i in range(num_iterations):
        gradient = compute_gradient(copy_weights)
        for weight in copy_weights:
            copy_weights[weight] = copy_weights[weight] - gradient[weight]*alpha
        if i%100 == 0:
            print(f'\nstep {i}')
            print('rss:', rss(copy_weights))
            print('weights:', copy_weights)
    return copy_weights

new_weights = descend(neuron_weights, 2000)
y_new = [predict(num,new_weights) for num in x]


plt.style.use('bmh')
plt.plot(x, y_new, label="Final Regression")
plt.legend()

plt.savefig('analysis/neural_net_regression.png')



print(rss(neuron_weights))












# class Neuron:
#     def __init__(self, index, parents=None, children=None, is_bias=False):
#         self.parents = parents
#         self.index = index
#         self.bias = is_bias
#         if is_bias:
#             self.children = None
#             self.output = 1
#         else:
#             self.children = children
#             self.output = None
    
#     def actv_func(self,neuron_input):
#         return max(0,neuron_input)
    
#     def set_output(neuron_input):
#         self.output = actv_func(neuron_input)


# class NeuralNet:
#     def __init__(self, input):
#         self.weight = 1
#         self.biases = [2,5]
#         self.neurons = [Neuron(i) if i not in self.biases else Neuron(i, is_bias=True) for i in range(1,7)]

#     def forward_propagate(self, initial_input):
#         for neuron in self.neurons:

#             print(neuron.index, neuron.bias)

# net = NeuralNet(1)
# net.forward_propagate(1)
