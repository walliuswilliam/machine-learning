import random
import matplotlib.pyplot as plt

def create_random_dataset():
  dataset = {1:[], 2:[]}
  for i in range(50):
    #X center (1,1)
    dataset[1].append([1+random.uniform(-2,2), 1+random.uniform(-2,2)])
    #X center (4,4)
    dataset[1].append([4+random.uniform(-2,2), 4+random.uniform(-2,2)])
    #Y center (1,4)
    dataset[2].append([1+random.uniform(-2,2), 4+random.uniform(-2,2)])
    #Y center (4,1)
    dataset[2].append([4+random.uniform(-2,2), 1+random.uniform(-2,2)])
  return dataset

if __name__ == "__main__":
  dataset = create_random_dataset()
  for i in range(100):
    plt.plot([dataset[1][i][0]], [dataset[1][i][1]], marker='o', color='red')
    plt.plot([dataset[2][i][0]], [dataset[2][i][1]], marker='x', color='blue')

  plt.savefig('datasets/semi_random.png')
