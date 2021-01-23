import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor:
  def __init__(self, df, dependent_variable, upper_bound):
    self.df = df
    self.upper_bound = upper_bound
    self.dependent_variable = dependent_variable
    self.independent_variables = [x for x in self.df.columns if x != self.dependent_variable]
    self.coefficients = self.calc_coefficients()
  

  def calc_coefficients(self):
    dict_data = self.df.data_dict
    dependent_var_column = dict_data[self.dependent_variable]

    for value_index in range(len(dependent_var_column)):
      y_transformed = math.log((self.upper_bound/dependent_var_column[value_index])-1)
      dict_data[self.dependent_variable][value_index] = y_transformed

    logistic_df = DataFrame(dict_data, [key for key in dict_data]) #column_order
    regressor = LinearRegressor(logistic_df, dependent_variable=self.dependent_variable)
    return regressor.coefficients

  def predict(self, input_dict):
    prediction = self.coefficients['constant']
    for coefficient in self.coefficients:
      if coefficient in input_dict.keys():
        prediction += self.coefficients[coefficient]*input_dict[coefficient]
    return self.upper_bound/(1+math.e**prediction)
    
    






  