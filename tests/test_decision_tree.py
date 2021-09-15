import sys
sys.path.append('src')
from decision_tree import DecisionTree


print('Data Set 1')
data = {1:[[2,1],[2,2],[3,2],[3,3]],2:[[2,3],[2,4],[3,4]]}
dt = DecisionTree(data)

dt.create_tree()

print('\ntesting predictions for data set 1...')
assert dt.predict([0, -1]) == 1
assert dt.predict([5, 6]) == 2
assert dt.predict([2, 3]) == 2
assert dt.predict([5, 3]) == 1
print('passed')


print('\n\n\nData Set 2')
data_2 = {1:[[2,2],[3,2]], 2:[[1,1],[2,1],[1,2]]}
dt_2 = DecisionTree(data_2)

dt_2.create_tree()

print('\ntesting predictions for data set 2...')
assert dt_2.predict([3, 2]) == 1
assert dt_2.predict([1, 3]) == 2
assert dt_2.predict([4, 4]) == 1
assert dt_2.predict([1, 10]) == 2
print('passed')

