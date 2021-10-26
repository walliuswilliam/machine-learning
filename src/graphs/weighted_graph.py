import sys
sys.path.append('src')
from graph import Graph

class Node:
  def __init__(self, index):
    self.index = index
    self.d_value = None
    self.neighbors = None

class WeightedGraph:
  def __init__(self, weights, vertex_values):
    self.weights = weights
    max_index = 0
    for (a,b) in self.weights.keys():
      if a > max_index or b > max_index:
        max_index = max(a,b)
    self.nodes = [Node(i) for i in range(max_index+1)]
    self.set_neighbors()

  def set_neighbors(self):
    for node in self.nodes:
      neighbor_list = []
      for pair in self.weights.keys():
        if pair[0] == node.index:
          neighbor_list.append(self.nodes[pair[1]])
        if pair[1] == node.index:
          neighbor_list.append(self.nodes[pair[0]])
      node.neighbors = neighbor_list

  def get_d_values(self, starting_node_index, ending_node_index):
    current_node = self.nodes[starting_node_index]
    for node in self.nodes:
      node.d_value = 9999999999
    current_node.d_value = 0

    visited = []
    while current_node.index != ending_node_index:
      for neighbor in current_node.neighbors:
        if neighbor not in visited:
          if (current_node.index, neighbor.index) in self.weights:
            new_d_value = current_node.d_value+self.weights[(current_node.index, neighbor.index)]
          else:
            new_d_value = current_node.d_value+self.weights[(neighbor.index, current_node.index)]
          if new_d_value < neighbor.d_value:
            neighbor.d_value = new_d_value

      visited.append(current_node)
      lowest_node = None

      for node in self.nodes:
        if node not in visited:
          if lowest_node is None:
            lowest_node = node
          elif node.d_value < lowest_node.d_value:
            lowest_node = node

      current_node = lowest_node


  def calc_distance(self, starting_node_index, ending_node_index):
    self.get_d_values(starting_node_index, ending_node_index)
    return self.nodes[ending_node_index].d_value

  def calc_shortest_path(self, start_node, end_node):
    edge_list = []
    self.get_d_values(start_node, end_node)

    for (a,b) in self.weights.keys():
      difference = abs(self.nodes[a].d_value - self.nodes[b].d_value)
      if difference == self.weights[(a,b)]:
        edge_list.append((a,b))
        
    graph = Graph(edge_list)
    return graph.calc_shortest_path(start_node, end_node)
