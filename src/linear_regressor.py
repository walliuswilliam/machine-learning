import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame

class LinearRegressor:
  def __init__(self, df, dependent_variable):
    self.df = df
    self.dependent_variable = dependent_variable
    self.coefficients = self.calculate_coefficients()
  
  def calculate_coefficients(self):
    final_dict = {}
    mat = Matrix([[1, num] for num in list(self.df.data_dict.values())[0][0]])
    mat_t = mat.transpose()
    mat_mult = mat_t.matrix_multiply(mat)
    mat_inv = mat_mult.inverse()
    mat_pseudoinv = mat_inv.matrix_multiply(mat_t)
    multiplier = [[num] for num in list(self.df.data_dict.values())[1][0]]
    multiplier_mat = mat_pseudoinv.matrix_multiply(Matrix(multiplier))
    for num in range(len(multiplier_mat.elements)):
      if num == 0:
        key = 'constant'
      else:
        key = list(self.df.data_dict.keys())[num]
        final_dict[key] = [row[0] for row in multiplier_mat.elements][num]
    return final_dict
  
  def predict(self, h_worked):
    return round(self.coefficients[0] + list(h_worked.values())[0]*self.coefficients[1], 5)
