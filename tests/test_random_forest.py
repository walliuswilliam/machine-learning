import sys
sys.path.append('src')
sys.path.append('datasets')
from random_forest import *
from semi_random import *
import random


# print('testing 5-fold CV accuracy')
# data = create_random_dataset()
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
#     if len(data[key]) == 0:
#       if key == 1:
#         key = 2
#       else:
#         key = 1
#     value_index = random.randint(0,len(data[key])-1)
#     chosen_point = data[key][value_index]
#     fold_dict[key].append(chosen_point)
#     data[key].pop(value_index)
#   folds.append(fold_dict)

# def dict_len(dic):
#   return len(sum(dic.values(),[]))

# num_trees = [1,10,20,50,100,500,1000]
# #num_trees = [1,5,10]
# accuracies = []

# for num_tree in num_trees:
#   num_classifications = 0
#   num_correct = 0
  
#   for fold in folds:
#     other_folds = [i for i in folds if i != fold]
#     train_data = merge_folds(other_folds)
#     forest = RandomForest(train_data)
#     forest.fit_trees(num_trees=num_tree)

#     for class_index in fold:
#       for value in fold[class_index]:
#         if forest.predict(value) == class_index:
#           num_correct += 1
#         num_classifications += 1
#   accuracy = num_correct/num_classifications
#   accuracies.append(accuracy)
#   print('finished num_tree {}'.format(num_tree))

# plt.plot(num_trees, accuracies)
# plt.xlabel('number of trees')
# plt.ylabel('5-fold accuracy')
# plt.savefig('forest_accuracy.png')



data = create_random_dataset()
folds = []

def merge_folds(fold_list):
  merged_folds = {}
  for class_num in folds[0]:
    class_list = []
    for fold in fold_list:
      class_list += fold[class_num]
    merged_folds[class_num] = class_list 
  return merged_folds


for fold_num in range(5):
  fold_dict = {1:[], 2:[]}
  for point_num in range(40):
    key = random.randint(1,2)
    if len(data[key]) == 0:
      if key == 1:
        key = 2
      else:
        key = 1
    value_index = random.randint(0,len(data[key])-1)
    chosen_point = data[key][value_index]
    fold_dict[key].append(chosen_point)
    data[key].pop(value_index)
  folds.append(fold_dict)

def dict_len(dic):
  return len(sum(dic.values(),[]))

num_trees = [1,10,20,50,100,500,1000]
#num_trees = [1,5,10]
accuracies = []

for num_tree in num_trees:
  num_classifications = 0
  num_correct = 0
  
  for fold in folds:
    other_folds = [i for i in folds if i != fold]
    train_data = merge_folds(other_folds)
    forest = RandomForest(train_data)
    forest.fit_trees(num_trees=num_tree,use_p=True, min_size=10)

    for class_index in fold:
      for value in fold[class_index]:
        if forest.predict(value) == class_index:
          num_correct += 1
        num_classifications += 1
  accuracy = num_correct/num_classifications
  accuracies.append(accuracy)
  print('finished num_tree {}'.format(num_tree))

plt.plot(num_trees, accuracies)
plt.xlabel('number of trees')
plt.ylabel('5-fold accuracy')
plt.savefig('forest_accuracy_2.png')