class Node:
  def __init__(self, index):
    self.index = index
    self.value = None
    self.children = None
    self.parents = None
    self.previous = None
    self.distance = None

class DirectedGraph:
  def __init__(self, edges):
    self.edges = edges
    max_index = 0
    for (a,b) in edges:
      if a > max_index or b > max_index:
        max_index = max(a,b)
    self.nodes = [Node(i) for i in range(max_index+1)]
    self.set_families()

  def set_families(self):
    for node in self.nodes:
      parents_list = []
      children_list = []
      for pair in self.edges:
        if pair[0] == node.index:
          children_list.append(self.nodes[pair[1]])
        if pair[1] == node.index:
          parents_list.append(self.nodes[pair[0]])
      node.parents = parents_list
      node.children = children_list


  def nodes_breadth_first(self, starting_index):
    for node in self.nodes:
      node.distance = 0
    queue = [self.nodes[starting_index]]
    visited = []
    while len(queue) != 0:
      node = queue[0]
      queue.remove(node)
      visited.append(node)
      for child in node.children:
        if child not in visited and child not in queue:
          queue.append(child)
          child.previous = node
          child.distance = node.distance + 1
    return visited

  def nodes_depth_first(self, starting_index):
    stack = [self.nodes[starting_index]]
    visited = []
    while len(stack) != 0:
      node = stack[0]
      stack.remove(node)
      visited.append(node)
      for child in node.children:
        if child not in visited and child not in stack:
          stack.insert(0, child)
    return visited

  def calc_distance(self, starting_node_index, ending_node_index):
    self.nodes_breadth_first(starting_node_index)
    return self.nodes[ending_node_index].distance

  def calc_shortest_path(self, starting_node_index, ending_node_index):
    self.nodes_breadth_first(starting_node_index)
    node = self.nodes[ending_node_index]
    shortest_path = [node]
    counter = 0
    
    while (node != self.nodes[starting_node_index]):
      if counter > len(self.nodes):
        return False
      node = node.previous
      shortest_path.append(node)
      counter += 1

    return [node.index for node in reversed(shortest_path)]
