import sys
sys.path.append('src/graphs')
from tree import Tree

node_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
edges = [(0,2), (4,6), (4,8), (4,0), (3,1), (0,3), (3,5), (5,7), (3,9), (3,10)]

# edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]

tree = Tree(edges, node_values)
tree.build_from_edges()


# print('finding the root...')
# assert tree.root.value == 'e'
# print('passed')

# print('finding children of "root"...')
# assert [node.value for node in tree.root.children] == ['g','i','a'], [node.value for node in tree.root.children]
# print('passed')

# print('finding children of "a"...')
# assert [node.value for node in tree.root.children[2].children] == ['c', 'd']
# print('passed')

# print('finding children of "i"...')
# assert [node.value for node in tree.root.children[1].children] == []
# print('passed')

# print('finding children of "g"...')
# assert [node.value for node in tree.root.children[0].children] == ['b']
# print('passed')

# print('finding children of "c"...')
# assert [node.value for node in tree.root.children[2].children[0].children] == ['k']
# print('passed')

# print('finding children of "d"...')
# assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j']
# print('passed')

# print('finding children of "b"...')
# assert [node.value for node in tree.root.children[0].children[0].children] == []
# print('passed')

# print('finding children of "k"...')
# assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []
# print('passed')

# print('finding children of "j"...')
# assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []
# print('passed')

# print('finding children of "f"...')
# assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h']
# print('passed')


print('testing nodes_breadth_first...')
nodes = tree.nodes_breadth_first()
assert {node.value for node in nodes} == {'e','g','i','a','b','c','d','k','f','j','h'}
print('passed')

print('testing nodes_breadth_first...')
nodes = tree.nodes_depth_first()
assert {node.value for node in nodes} == {'e','a','d','j','f','h','c','k','i','g','b'}
print('passed')

print('\nTEST CASE 1')
children = set(tree.root.children)

grandchildren = set([])
for child in children:
  grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
  great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
  great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

print('testing node indices and values...')
assert {node.index for node in children} == {0, 8, 6}
assert {node.value for node in children} == {'a', 'i', 'g'}

assert {node.index for node in grandchildren} == {2, 3}
assert {node.value for node in grandchildren} == {'c', 'd'}

assert {node.index for node in great_grandchildren} == {1, 9, 5, 10}
assert {node.value for node in great_grandchildren} == {'b', 'j', 'f', 'k'}

assert {node.index for node in great_great_grandchildren} == {7}
assert {node.value for node in great_great_grandchildren} == {'h'}
print('passed')


print('\nTEST CASE 2')

node_values = ['a', 'b', 'a', 'a', 'a', 'b', 'a', 'b', 'a', 'b', 'b']
edges = [(0,2), (4,6), (4,8), (4,0), (3,1), (0,3), (3,5), (5,7), (3,9), (3,10)]

tree = Tree(edges, node_values)
tree.build_from_edges()


assert tree.root.value == 'a'
assert tree.root.index == 4

children = set(tree.root.children)

grandchildren = set([])
for child in children:
  grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
  great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
  great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

print('testing node indices and values...')
assert {node.index for node in children} == {0, 8, 6}
assert {node.value for node in children} == {'a', 'a', 'a'}

assert {node.index for node in grandchildren} == {2, 3}
assert {node.value for node in grandchildren} == {'a', 'a'}

assert {node.index for node in great_grandchildren} == {1, 9, 5, 10}
assert {node.value for node in great_grandchildren} == {'b', 'b', 'b', 'b'}

assert {node.index for node in great_great_grandchildren} == {7}
assert {node.value for node in great_great_grandchildren} == {'b'}
print('passed')
