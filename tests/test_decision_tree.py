import sys
sys.path.append('src')
sys.path.append('datasets')
from decision_tree import *
from semi_random import *
import random


# print('Data Set 1')
# data = {1:[[2,1],[2,2],[3,2],[3,3]],2:[[2,3],[2,4],[3,4]]}
# dt = DecisionTree(data)

# dt.create_tree()

# print('\ntesting predictions for data set 1...')
# assert dt.predict([0, -1]) == 1
# assert dt.predict([5, 6]) == 2
# assert dt.predict([2, 3]) == 2
# assert dt.predict([5, 3]) == 1
# print('passed')


# print('\n\n\nData Set 2')
# data_2 = {1:[[2,2],[3,2]], 2:[[1,1],[2,1],[1,2]]}
# dt_2 = DecisionTree(data_2)

# dt_2.create_tree()

# print('\ntesting predictions for data set 2...')
# assert dt_2.predict([3, 2]) == 1
# assert dt_2.predict([1, 3]) == 2
# assert dt_2.predict([4, 4]) == 1
# assert dt_2.predict([1, 10]) == 2
# print('passed')


#Min size tests

#X = 1, O = 2
# print('\n\nTesting Impure, Non-Tie Test Case')
# data = {1:[[1,7],[2,7],[3,7],[3,8],[3,9],[7,1]],2:[[5,1],[5,2],[5,3],[6,3],[7,3],[1,9]]}
# dt = DecisionTree(data, min_size_to_split=7, rand_seed=0)

# dt.create_tree()

# assert dt.predict([2, 8]) == 1
# assert dt.predict([6, 2]) == 2
# assert dt.predict([-10, 2]) == 1
# assert dt.predict([100, 2]) == 2

# assert dt.nodes[0].children[0].children == None
# assert dt.nodes[0].children[1].children == None
# print('passed')


# print('\n\nTesting Pure, Tie Test Case')
# data = {1:[[1,3],[1,5],[2,4],[2,5]],2:[[1,4],[2,3]]}
# dt = DecisionTree(data, min_size_to_split=5, rand_seed=0)

# dt.create_tree()

# assert dt.predict([2, 8]) == 1
# assert dt.predict([-10, 100]) == 1
# assert dt.predict([2, 5]) == 1
# assert dt.predict([0, 10]) == 1

# assert dt.nodes[0].children[0].children == None
# assert dt.nodes[0].children[1].children == None
# print('passed')


# print('\n\ntesting multiple classes on a point...')
# data = {1:[[0,1],[0,1],[0,2],[1,1],[1,2],[1,2]],2:[[0,2],[1,1],[1,1],[1,2]]}
# dt = DecisionTree(data,rand_seed=0)
# dt.create_tree()

# print([node.points for node in dt.nodes])

# print('0,0')
# assert dt.predict([0, 0]) == 1
# print('0,2')
# assert dt.predict([0, 2]) == 2 #random
# print('10,0')
# assert dt.predict([10, 0]) == 2
# assert dt.predict([0, 8]) == 1
# print('passed')


# print('\n\ntesting 5-fold cross validation accuracy')
# dataset = create_random_dataset()

# folds = []


# def merge_folds(fold_list):
#   merged_folds = {}
#   for class_num in folds[0]:
#     class_list = []
#     for fold in fold_list:
#       class_list += fold[class_num]
#     merged_folds[class_num] = class_list 
#   return merged_folds


# for fold_num in range(5):
#   fold_dict = {1:[], 2:[]}
#   for point_num in range(40):
#     key = random.randint(1,2)
#     if len(dataset[key]) == 0:
#       if key == 1:
#         key = 2
#       else:
#         key = 1
#     value_index = random.randint(0,len(dataset[key])-1)
#     chosen_point = dataset[key][value_index]
#     fold_dict[key].append(chosen_point)
#     dataset[key].pop(value_index)
#   folds.append(fold_dict)

# def dict_len(dic):
#   return len(sum(dic.values(),[]))

# min_splits = [1,2,5,10,15,20,30,50,100]
# accuracies = []

# for min_split in min_splits:
#   num_classifications = 0
#   num_correct = 0
  
#   for fold in folds:
#     other_folds = [i for i in folds if i != fold]
#     train_data = merge_folds(other_folds)
#     dt = DecisionTree(train_data, min_size_to_split=min_split, debug=False)
#     dt.create_tree()

#     for class_index in fold:
#       for value in fold[class_index]:
#         if dt.predict(value) == class_index:
#           num_correct += 1
#         num_classifications += 1
#   accuracy = num_correct/num_classifications
#   accuracies.append(accuracy)

# plt.plot(min_splits, accuracies)
# plt.xlabel('min_size_split')
# plt.ylabel('5-fold accuracy')
# plt.savefig('decision_min_size_vs_acc.png')


data = {1:[[2,1],[2,2],[3,2],[3,3]],2:[[2,3],[2,4],[3,4]]}

dt = DecisionTree(data)
#dt = DecisionTree(data, random=True)

dt.create_tree()

