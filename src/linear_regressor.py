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
    mat = [[1 for x in list(self.df.data_dict.values())[0][0]]]
    mat_dict = {}
    for key in self.df.data_dict:
      if key != self.dependent_variable:
        mat_dict[key] = self.df.data_dict[key]
    for row in range(len(mat_dict)):
      mat.append(list(self.df.data_dict.values())[row][0])
    mat = Matrix(mat)
    mat = mat.transpose()
    print('mat', mat.elements)
    mat_t = mat.transpose()
    print('mat_t', mat_t.elements)
    mat_mult = mat_t.matrix_multiply(mat)
    print('mat_mult', mat_mult.elements)
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



