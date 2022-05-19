import sys, os, pkg_resources, math
pkgs = sorted([str(i.key) for i in pkg_resources.working_set])
if 'matplotlib' not in pkgs: os.system("pip install matplotlib")
import matplotlib.pyplot as plt, time
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

start = time.time()

num_gens = 5
avg_rss = []
first_gen = create_initial_generation([1,10,6,3,1], data, lambda x: math.tanh(x))
stop = time.time()

print('initial creation', stop-start)

current_gen = first_gen
for _ in range(num_gens):
  start = time.time()
  avg_rss.append(get_avg_rss(current_gen))
  stop = time.time()
  print('avg rss', stop-start)
  start = time.time()
  current_gen = create_new_generation(current_gen)
  stop = time.time()
  print('new gen', stop-start)
  print('gen', _, '\n')


plt.plot(list(range(num_gens)), avg_rss)
plt.title('Evolving Neural Net')
plt.xlabel('Num Generation')
plt.ylabel('Avg RSS')
plt.savefig('evolving_neural_nets/rss_values.png')
