import sys
sys.path.append('src')
from decision_tree import *

class RandomForest:
  def __init__(self, data, num_trees=100, min_size=1):
    self.data = data
    self.forest = [DecisionTree(self.data,min_size_to_split=min_size,random=True,debug=False) for i in range(num_trees)]
    for tree in self.forest:
      tree.create_tree()

  def predict(self, point, debug=False):
    predictions = {}
    for tree in self.forest:
      prediction = tree.predict(point)
      if prediction in predictions.keys():
        predictions[prediction] += 1
      else:
        predictions[prediction] = 1
    if debug:
      print(predictions)
    return max(predictions, key=predictions.get)
