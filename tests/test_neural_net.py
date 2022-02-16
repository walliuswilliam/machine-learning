import sys
sys.path.append('src')
from neural_net import NeuralNet


data = [(-5,-3),(-4,-1),(-3,1),(-2,2),(-1,-1),(1,-1),(2,1),(3,2),(4,3),(5,4),(6,2),(7,0)]
weights = {(3,1):0,
           (4,1):0,
           (3,2):0,
           (4,2):0,
           (6,3):0,
           (6,4):0,
           (6,5):0,
           (7,3):0,
           (7,4):0,
           (7,5):0,
           (9,6):0,
           (9,7):0,
           (9,8):0}

for edge in weights:
  k, j = edge
  weights[edge] = ((-1)**(j+k))*min(j,k)/max(j,k)

net = NeuralNet(weights, data, lambda x: max(0,x), 9, [2,5,8])

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