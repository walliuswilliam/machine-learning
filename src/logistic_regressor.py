import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor:
  def __init__(self, df, dependent_variable):
    self.df = df
    self.dependent_variable = dependent_variable
    self.independent_variables = [x for x in self.df.columns if x != self.dependent_variable]
    self.coefficients = self.calc_coefficients()

  def calc_coefficients(self):
    dict_data = self.df.data_dict
    independent_variable = self.independent_variables[0]
    transformed_mat = [[value] for value in dict_data[independent_variable]]
    y_list = []
    print(transformed_mat)
    for variable in dict_data:
      if variable == self.dependent_variable:
        variable_list = dict_data[variable]
        for value in variable_list:
          y_transformed = math.log((1/value)-1)
          y_list.append(y_transformed)

    for y_index in range(len(y_list)):
      transformed_mat[y_index].append(y_list[y_index])
    print(transformed_mat)

    






  