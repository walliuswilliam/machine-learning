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
    try:
      self.coefficients = self.calc_coefficients()
    except:
      self.coefficients = {}
  

  def calc_coefficients(self):
    dict_data = self.df.data_dict
    dependent_var_column = dict_data[self.dependent_variable]

    for value_index in range(len(dependent_var_column)):
      y_transformed = math.log((self.upper_bound/dependent_var_column[value_index])-1)
      dict_data[self.dependent_variable][value_index] = y_transformed

    logistic_df = DataFrame(dict_data, self.df.columns)
    regressor = LinearRegressor(logistic_df, dependent_variable=self.dependent_variable)
    return regressor.coefficients

  def predict(self, input_dict):
    for variable in self.independent_variables:
      if '*' not in variable and variable not in input_dict:
        input_dict[variable] = 0
      if ' * ' in variable:
        interaction_terms = variable.split(' * ')
        input_dict[variable] = input_dict[interaction_terms[0]]*input_dict[interaction_terms[1]]
    
    prediction = self.coefficients['constant']
    for coefficient in self.coefficients:
      if coefficient in input_dict.keys():
        prediction += self.coefficients[coefficient]*input_dict[coefficient]
    return self.upper_bound/(1+math.exp(prediction))
  

  #gradient descent

  def set_coefficients(self, coeffs):
    self.coefficients = coeffs

  def calc_rss(self):
    rss_sum = 0
    for (a,b) in self.df.to_array():
      rss_sum += (b-self.predict({'x': a}))**2
    return rss_sum

  def calc_gradient(self, delta):
    final_dict = {}
    for coefficient in self.coefficients:
      original_coefs = self.coefficients.copy()
      forward_coefs = self.coefficients.copy()
      backward_coefs = self.coefficients.copy()

      forward_coefs[coefficient] += delta
      backward_coefs[coefficient] -= delta

      self.set_coefficients(forward_coefs)
      forward_rss = self.calc_rss()

      self.set_coefficients(backward_coefs)
      backward_rss = self.calc_rss()

      self.set_coefficients(original_coefs)
      coef_gradient = (forward_rss-backward_rss)/(2*delta)
      final_dict[coefficient] = coef_gradient
    
    return final_dict
    
  def gradient_descent(self, alpha, delta, num_steps, debug_mode=False):
    for num in range(num_steps):
      if debug_mode:
        print('\nstep {}:'.format(num))
        print('gradient =', {key:round(self.calc_gradient(delta)[key],4) for key in self.calc_gradient(delta)})
        print('coeffs =', {key:round(self.coefficients[key],4) for key in self.coefficients})
        print('rss =', round(self.calc_rss(),4))
      for coefficient in self.coefficients:
        self.coefficients[coefficient] = self.coefficients[coefficient] - alpha*self.calc_gradient(delta)[coefficient]
      
          

