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
    mat = Matrix(mat_elements)
    mat = mat.transpose()
    
    # mat * beta = y
    # (mat_t * mat) * beta = mat_t * y
    # beta = (mat_t * mat)^-1 * mat_t * y
    mat_t = mat.transpose()
    mat_mult = mat_t.matrix_multiply(mat)
    mat_inv = mat_mult.inverse()
    mat_pseudoinv = mat_inv.matrix_multiply(mat_t)
    y = [[num] for num in dict_data[self.dependent_variable]]
    y_mat = mat_pseudoinv.matrix_multiply(Matrix(y)) #coefficients


    for coefficient_index in range(len(y_mat.elements)):
      if coefficient_index == 0:
        key = 'constant'
      else:
        key = self.independent_variables[coefficient_index-1] #constant takes up first spot, everything shifts over one index
      final_dict[key] = [coefficient[0] for coefficient in y_mat.elements][coefficient_index]

    return final_dict

  def predict(self, h_worked):
    return round(self.coefficients[0] + list(h_worked.values())[0]*self.coefficients[1], 5)