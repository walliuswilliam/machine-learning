import sys
sys.path.append('src')
from decision_tree import *
import random as rand

class RandomForest:
  def __init__(self, data, p=80):
    self.data = data
    self.forest = None
    self.p = p
  
  def fit_trees(self, num_trees=100, min_size=1, use_p=False):
    if not use_p:
      self.forest = [DecisionTree(self.data,min_size_to_split=min_size,random=True,debug=False) for i in range(num_trees)]
    if use_p:
      num_data_points = round((self.p/100)*len(sum(self.data.values(),[])))
      self.forest = []
      for num in range(num_trees):
        data = self.split_data(num_data_points)
        self.forest.append(DecisionTree(data,min_size_to_split=min_size,debug=False))
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
  
  def split_data(self,num_points):
    new_data = {key:[] for key in self.data.keys()}
    new_data_len = len(sum(new_data.values(),[]))
    while new_data_len != num_points:
      rand_key = rand.choice(list(self.data.keys()))
      rand_value = rand.choice(self.data[rand_key])

      if rand_value not in new_data[rand_key]:
        new_data[rand_key].append(rand_value)
      new_data_len = len(sum(new_data.values(),[]))
    return new_data  

