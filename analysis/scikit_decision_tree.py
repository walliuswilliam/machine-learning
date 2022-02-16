import sys
sys.path.append('datasets')
from semi_random import *
import random

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



# print('testing 5-fold CV accuracy')
# data = create_random_dataset(200)

# num_trees = [1,10,20,50,100,500,1000]
# accuracies = []

# for num_tree in num_trees:
#   X_train, X_test, y_train, y_test = train_test_split(data[0],data[1],test_size=0.2)
#   forest = RandomForestClassifier(n_estimators=num_tree)
#   forest.fit(X_train, y_train)
#   accuracies.append(accuracy_score(y_test,forest.predict(X_test)))
#   print('finished num_tree {}'.format(num_tree))

# plt.plot(num_trees, accuracies)
# plt.xlabel('number of trees')
# plt.ylabel('5-fold accuracy')
# plt.savefig('scikit_forest_accuracy.png')






data = create_random_dataset(200)
X_train, X_test, y_train, y_test = train_test_split(data[0],data[1],test_size=0.5)



forest = RandomForestClassifier(n_estimators=100)
forest.fit(X_train, y_train)


random_points = [[random.uniform(-6,6),random.uniform(-6,6)] for num in range(2500)]

pred = forest.predict(random_points)

pred = ['salmon' if num==1 else 'cornflowerblue' for num in pred]
x, y = zip(*random_points)
plt.scatter(x,y, s=20, c=pred)

y_test = ['red' if num==1 else 'blue' for num in y_test]
x, y = zip(*X_test)
plt.scatter(x,y,s=75, c=y_test)

# pred = forest.predict(X_test)

# x, y = zip(*X_test)
# plt.scatter(x,y, c=pred)




plt.savefig('scikit_forest_scatter_plot.png')
print('done')
