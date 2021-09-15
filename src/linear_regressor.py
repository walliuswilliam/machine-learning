import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame

class LinearRegressor:
  def __init__(self, df, dependent_variable):
    self.df = df
    self.dependent_variable = dependent_variable
    self.independent_variables = [x for x in self.df.columns if x != self.dependent_variable]
    self.coefficients = self.calculate_coefficients()
  
  def calculate_coefficients(self):
    final_dict = {}
    dict_data = self.df.data_dict

    observations_of_a_variable = list(dict_data.values())[0] # [obs1, obs2, obs3, ...] - initialize matrix elements with a row of 1s
    row_of_1s = [1 for _ in observations_of_a_variable] 
    mat_elements = [row_of_1s]

    # add the rows of observations for the independent_variables
    for variable_name in dict_data:
      if variable_name != self.dependent_variable:
        observations = dict_data[variable_name]
        mat_elements.append(observations)
    mat = Matrix(mat_elements).transpose()
    print(mat.elements)
    
    # mat * beta = y
    # (mat_t * mat) * beta = mat_t * y
    # beta = (mat_t * mat)^-1 * mat_t * y
    mat_t = mat.transpose()
    mat_mult = mat_t @ mat #matrix multiply
    mat_inv = mat_mult.inverse()
    mat_pseudoinv = mat_inv @ mat_t #matrix multiply
    y = [[num] for num in dict_data[self.dependent_variable]]

    coefficients = (mat_pseudoinv @ Matrix(y)).transpose().elements[0]
    final_dict = {'constant' :  coefficients[0]}

    for coefficient_index in range(len(self.independent_variables)):
      key = self.independent_variables[coefficient_index]
      final_dict[key] = coefficients[coefficient_index + 1]
      
    return final_dict

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
    return prediction
