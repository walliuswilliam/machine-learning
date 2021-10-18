import pandas as pd
import math
import random as rand

class DecisionTree:
  def __init__(self, data, min_size_to_split=1, rand_seed=None, debug=True, random=False):
    self.data = data
    self.all_points = sum(self.data.values(), [])
    self.nodes = [Node(self.data)]
    self.min_size = min_size_to_split
    if rand_seed is not None:
      rand.seed(rand_seed)
    self.debug = debug
    self.random = random
    

  def find_splits(self, node):
    node_points = sum(node.points.values(), [])
    for num in range(len(node_points[0])):
      unique_values = []
      for point in node_points:
        if point[num] not in unique_values:
          unique_values.append(point[num])
      unique_values.sort()
      unique_values = pd.Series(unique_values)
      splits_nans = unique_values.rolling(2).mean().tolist()
      splits = [x for x in splits_nans if math.isnan(x) == False]
      node.splits.append(splits)
  
  def choose_best_split(self, node):
    if self.random is False:
      best_split = None
      best_avg = 1
      split_nodes = []

      for axis in range(len(node.splits)):
        for split in node.splits[axis]:
          greater_eq = {}
          less = {}

          for key, value in node.points.items():
            for point in value:
              if point[axis] >= split:
                if key in greater_eq.keys():
                  greater_eq[key].append(point)
                else:
                  greater_eq[key] = [point]
              else:
                if key in less.keys():
                  less[key].append(point)
                else:
                  less[key] = [point]

          g = Node(greater_eq)
          l = Node(less)
          g.entropy = self.find_entropy(g)
          l.entropy = self.find_entropy(l)
          weight_avg = self.calc_weighted_avg(g,l)

          if weight_avg < best_avg:
            best_avg = weight_avg
            best_split = (axis, split)
            split_nodes = [g,l]
      if self.debug:
        print('best split =', best_split)
      node.best_split = best_split
      return split_nodes
    else:
      splits = {}
      for i in range(len(node.splits)):
        splits[i] = node.splits[i]
      
      splits = {k:v for k,v in splits.items() if v}
      axis = rand.choice(list(splits.keys()))
      split = rand.choice(splits[axis])

      greater_eq = {}
      less = {}

      for key, value in node.points.items():
        for point in value:
          if point[axis] >= split:
            if key in greater_eq.keys():
              greater_eq[key].append(point)
            else:
              greater_eq[key] = [point]
          else:
            if key in less.keys():
              less[key].append(point)
            else:
              less[key] = [point]

      g = Node(greater_eq)
      l = Node(less)
      g.entropy = self.find_entropy(g)
      l.entropy = self.find_entropy(l)
      weight_avg = self.calc_weighted_avg(g,l)

      split_nodes = [g,l]
      if self.debug:
        print('random split =', (axis, split))
      node.best_split = (axis, split)
      return split_nodes
      
  def create_split(self, parent_node, split_nodes):
    parent_node.children = split_nodes
    self.nodes += split_nodes

  def create_tree(self):
    queue = [self.nodes[0]]
    while len(queue) != 0:
      curr_node = queue[0]
      if curr_node.size <= self.min_size:
        queue.pop(0)
        continue

      if self.debug:
        print('\ncurrent node points', curr_node.points)
      self.find_splits(curr_node)
      split_nodes = self.choose_best_split(curr_node)
      curr_node.entropy = self.find_entropy(curr_node)
      if self.debug:
        print('node entropy', curr_node.entropy)

      if curr_node.entropy == 0:
        queue.pop(0)
        continue

      else:
        self.create_split(curr_node, split_nodes)
        queue.pop(0)
        queue += split_nodes
      
  def calc_weighted_avg(self, node1, node2):
    num_points_1 = len(sum(node1.points.values(), []))
    num_points_2 = len(sum(node2.points.values(),[]))
    total_num_points = num_points_1+num_points_2
    return ((num_points_1/total_num_points)*node1.entropy + (num_points_2/total_num_points)*node2.entropy)

  def find_entropy(self,node):
    entropy = 0
    for class_ in self.data.keys():
      total_points = 0
      for point in sum(node.points.values(), []):
        if point in self.data[class_]:
          total_points += 1
      p = total_points/node.size
      if p != 0:
        entropy -= p*math.log(p)
    return entropy

  def predict(self, point):
    point_class = None
    current_node = self.nodes[0]
    while point_class == None:
      if current_node.children == None:
        curr = current_node.points
        val_len = [(key, len(curr[key])) for key in curr]
        max_len = list(map(max, zip(*val_len)))[1]
        
        classes = []
        for key_count in val_len:
          if key_count[1] == max_len:
            classes.append(key_count[0])
        point_class = classes[rand.randint(0,len(classes)-1)] 
        break
      axis,split = current_node.best_split
      if point[axis] >= split: 
        current_node = current_node.children[0]
      else:
        current_node = current_node.children[1]
    return point_class


class Node():
  def __init__(self, points):
    self.points = points
    self.entropy = None
    self.children = None
    self.splits = []
    self.best_split = None
    self.size = len(sum(self.points.values(),[]))
