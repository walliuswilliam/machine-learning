import sys
sys.path.append('src/graphs')
from weighted_graph import WeightedGraph


weights = {
    (0,1): 3,
    (1,7): 4,
    (7,2): 2,
    (2,5): 1,
    (5,6): 8,
    (0,3): 2,
    (3,2): 6,
    (3,4): 1,
    (4,8): 8,
    (8,0): 4
}

vertex_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
weighted_graph = WeightedGraph(weights, vertex_values)


print('testing calc_distance...')
assert weighted_graph.calc_distance(8,4) == 7, weighted_graph.calc_distance(8,4)
assert [weighted_graph.calc_distance(8,n) for n in range(9)] == [
  4, 7, 12, 6, 7, 13, 21, 11, 0]
print('passed')

print('testing calc_shortest_path...')
assert weighted_graph.calc_shortest_path(8,4) == [8, 0, 3, 4]
assert weighted_graph.calc_shortest_path(8,7) == [8, 0, 1, 7]
assert weighted_graph.calc_shortest_path(8,6) == [8, 0, 3, 2, 5, 6]
print('passed')
