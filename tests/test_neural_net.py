import sys
sys.path.append('src')
from neural_net import NeuralNet
import matplotlib.pyplot as plt


def normalize(data_list):
  normalized_data = []
  min_x, min_y = min(data_list)
  max_x, max_y = max(data_list)
  for point in data_list:
    normalized_data.append(((point[0]-min_x)/(max_x-min_x), (point[1]-min_y)/(max_y-min_y)))
  return normalized_data


data = [(-5,-3),(-4,-1),(-3,1),(-2,2),(-1,-1),(1,-1),(2,1),(3,2),(4,3),(5,4),(6,2),(7,0)]
data = normalize(data)
weights = {(1,3):0,
           (1,4):0,
           (2,3):0,
           (2,4):0,
           (3,6):0,
           (4,6):0,
           (5,6):0,
           (3,7):0,
           (4,7):0,
           (5,7):0,
           (6,9):0,
           (7,9):0,
           (8,9):0}

for edge in weights:
  k, j = edge
  weights[edge] = ((-1)**(j+k))*min(j,k)/max(j,k)

net = NeuralNet(weights, data, lambda x: max(0,x), 9, [2,5,8])
# net.change_neuron_actv_func(9, lambda x: x)

net.gradient_descent(1)
print(net.weights, '\n')

inputs = [i/100 for i in range(0,1000)]
outputs = [net.predict(num) for num in inputs]

plt.clf()
plt.style.use('bmh')
plt.title("Neural Network Regression")
plt.scatter(*zip(*data), label='Datapoints')
plt.plot(inputs, outputs, label="Initial Regression")


RSS_vals = net.gradient_descent(2000, alpha=0.001, return_rss=True)

outputs = [net.predict(num) for num in inputs]

plt.plot(inputs, outputs, label="Final Regression")
plt.xlabel('Inputs')
plt.ylabel('Outputs')
plt.legend()
plt.savefig('NN_9_Neuron_Regression.png')

plt.clf()
plt.title("Neural Network RSS")
plt.plot([100*i for i in range(20)], RSS_vals)
plt.xlabel('Number of Iterations')
plt.ylabel('RSS')
plt.savefig('NN_9_Neuron_RSS.png')
