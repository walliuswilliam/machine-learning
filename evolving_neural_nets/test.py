import sys, os, pkg_resources, math
pkgs = sorted([str(i.key) for i in pkg_resources.working_set])
if 'matplotlib' not in pkgs: os.system("pip install matplotlib")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
sys.path.append('evolving_neural_nets')
from evolve_neural_net import *

data = [(0.0, 7), (0.2, 5.6), (0.4, 3.56), (0.6, 1.23), (0.8, -1.03),
 (1.0, -2.89), (1.2, -4.06), (1.4, -4.39), (1.6, -3.88), (1.8, -2.64),
 (2.0, -0.92), (2.2, 0.95), (2.4, 2.63), (2.6, 3.79), (2.8, 4.22),
 (3.0, 3.8), (3.2, 2.56), (3.4, 0.68), (3.6, -1.58), (3.8, -3.84),
 (4.0, -5.76), (4.2, -7.01), (4.4, -7.38), (4.6, -6.76), (4.8, -5.22)]


def normalize(data):
  normalized_data = []
  min_x, min_y = min(data)
  max_x, max_y = max(data)
  for point in data:
    normalized_data.append(((point[0]-min_x)/(max_x-min_x), (point[1]-min_y)/(max_y-min_y)))
  return normalized_data
  
data = normalize(data)

num_gens = 2000
avg_rss = []
first_gen = create_initial_generation([1,10,6,3,1], data, lambda x: math.tanh(x))

current_gen = first_gen
for _ in range(num_gens):
  avg_rss.append(get_avg_rss(current_gen))
  current_gen = create_new_generation(current_gen)
  if _%50==0:
    print('gen', _)

plt.plot(list(range(num_gens)), avg_rss)
plt.title('Evolving Neural Net')
plt.xlabel('Num Generation')
plt.ylabel('Avg RSS')
plt.savefig('evolving_neural_nets/rss_values.png')
plt.clf()


x_values = []
for i in range(1):
    for j in range(0,101):
        x_values.append(i+j*0.01)

for net in first_gen:
  y_values = []
  for x in x_values:
    y_values.append(net.predict(x))
  plt.plot(x_values, y_values, color='blue')

for net in current_gen:
  y_values = []
  for x in x_values:
    y_values.append(net.predict(x))
  plt.plot(x_values, y_values, color='red')

plt.scatter([p[0] for p in data], [p[1] for p in data], color='green')
custom_lines = [Line2D([0], [0], color='blue', lw=4),
                Line2D([0], [0], color='red', lw=4),
                Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=12)]
plt.legend(custom_lines, ['Initial Gen', f'Final Gen ({num_gens})', 'Data'])
plt.title('Evolving Neural Net')
plt.xlabel('X')
plt.ylabel('Predicted Value')
plt.savefig('evolving_neural_nets/evolved_networks.png')
