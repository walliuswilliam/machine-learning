import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor

class PolynomialRegressor:
  def __init__(self, degree):
    self.degree = degree
    self.df = None
    self.dependent_variable = None
    self.independent_variables = None
    self.coefficients = None
  

  def fit(self, df, dependent_variable):
    self.df = df.copy()
    self.dependent_variable = dependent_variable
    self.independent_variables = [x for x in self.df.columns if x != self.dependent_variable]

    for num in range(self.degree+1):
      if num > 1:
        degree_list = []
        for value in self.df.data_dict[self.independent_variables[0]]:
          degree_list.append(value**num)
        self.df.data_dict[str(self.independent_variables[0])+'^'+str(num)] = degree_list
        self.df.columns.append(str(self.independent_variables[0])+'^'+str(num))
    
    if self.degree == 0:
      del self.df.data_dict[self.independent_variables[0]]
      self.independent_variables.remove(self.independent_variables[0])
    if self.degree != 0:
      self.independent_variables = [x for x in self.df.columns if x != self.dependent_variable]
    
    self.coefficients = self.calculate_coefficients()
    


  def calculate_coefficients(self):
    final_dict = {}
    dict_data = self.df.data_dict

    observations_of_a_variable = list(dict_data.values())[0]
    row_of_1s = [1 for _ in observations_of_a_variable] 
    mat_elements = [row_of_1s]

    for variable_name in dict_data:
      if variable_name != self.dependent_variable:
        observations = dict_data[variable_name]
        mat_elements.append(observations)
    mat = Matrix(mat_elements)
    mat = mat.transpose()    
    mat_t = mat.transpose()
    mat_mult = mat_t @ mat
    mat_inv = mat_mult.inverse()
    mat_pseudoinv = mat_inv @ mat_t
    y = [[num] for num in dict_data[self.dependent_variable]]

    coefficients = (mat_pseudoinv @ Matrix(y)).transpose().elements[0]
    final_dict = {'constant' :  coefficients[0]}

    for coefficient_index in range(len(self.independent_variables)):
      key = self.independent_variables[coefficient_index]
      final_dict[key] = coefficients[coefficient_index + 1]
      
    return final_dict

  def predict(self, input_dict):
    for variable in self.independent_variables:
      if '^' in variable:
        interaction_terms = variable.split('^')
        input_dict[variable] = input_dict[interaction_terms[0]]**int(interaction_terms[1])
    
    prediction = self.coefficients['constant']
    for coefficient in self.coefficients:
      if coefficient in input_dict.keys():
        prediction += self.coefficients[coefficient]*input_dict[coefficient]
    return prediction
