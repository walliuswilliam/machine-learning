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
    mat = []
    for row in range(len(self.df.data_dict.values())):
      mat_row = [1]
      for column_name in self.df.columns:
        if column_name != self.dependent_variable:
          print('column_name', column_name)
          mat_row.append(self.df.select_columns(column_name))
      mat.append(mat_row)
    mat_t = mat.transpose()
    print('mat_t', mat_t.elements)
    mat_mult = mat_t.matrix_multiply(mat)
    print('mat_mult', mat_mult.elements)
    mat_inv = mat_mult.inverse()
    print('mat_inv', mat_inv.elements)
    mat_pseudoinv = mat_inv.matrix_multiply(mat_t)
    print('mat_pseudoinv', mat_pseudoinv.elements)
    multiplier = [[num] for num in list(self.df.data_dict.values())[1][0]]
    print('multiplier', multiplier)
    multiplier_mat = mat_pseudoinv.matrix_multiply(Matrix(multiplier))
    print('multiplier_mat', multiplier_mat.elements)
    
    for num in range(len(multiplier_mat.elements)):
      print('num', num)
      print(multiplier_mat.elements)
      if num == 0:
        key = 'constant'
      else:
        key = list(self.df.data_dict.keys())[num]
      final_dict[key] = [row[0] for row in multiplier_mat.elements][num]
    return final_dict
  
  def predict(self, h_worked):
    return round(self.coefficients[0] + list(h_worked.values())[0]*self.coefficients[1], 5)
