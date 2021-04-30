import pandas as pd
import numpy as np
import math
from collections import Counter

class KNearestNeighborsClassifier:
  def __init__(self, k):
    self.k = k
  
  def fit(self, df, dependent_variable):
    self.df = df
    self.dependent_variable = dependent_variable
    self.dv_index = self.df.columns[0].index(self.dependent_variable)
    self.independent_varibles = [x for x in self.df.columns if x != self.dependent_variable]

  def compute_distances(self, observation):
    independent_df = self.df[self.independent_varibles].copy()
    distances = []
    for row_index in range(len(independent_df.to_numpy())):
      distance = 0
      for variable in independent_df:
        distance += (self.df.iloc[row_index][variable] - observation[variable])**2
      distances.append(math.sqrt(distance))
    self.df['Distance'] = distances
    return self.df[[self.dependent_variable, 'Distance']]
   
  
  def nearest_neighbors(self, observation):
    self.df = self.compute_distances(observation)
    return self.df.sort_values(by=['Distance'])

  def classify(self, observation):
    self.df = self.nearest_neighbors(observation)[:self.k]
    c = Counter(self.df[self.dependent_variable])
    majority_list = c.most_common()
    tie = False
    for value, count in majority_list[1:]:
      if count == majority_list[0][1]:
        tie = True
    if not tie:
      return majority_list[0][0]
    else:
      average_list = []
      for variable in self.df[self.dependent_variable].unique():
        average = self.df.loc[self.df[self.dependent_variable] == variable].mean()[0]
        average_list.append((variable, average))
      return min(average_list, key=lambda x: x[1])[0]
      


