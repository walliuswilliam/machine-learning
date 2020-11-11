class Matrix:
  def __init__(self, elements):
    self.elements = elements
    self.num_rows = len(elements)
    self.num_cols = len(elements[0])
  
  #OVERLOADING
  def __add__(self, matrix2):
    return self.add(matrix2)
  def __sub__(self, matrix2):
    return self.subtract(matrix2)
  def __mul__(self, scalar):
    return self.scalar_multiply(scalar)
  def __matmul__(self, matrix2):
    return self.matrix_multiply(matrix2)
  def __eq__(self, matrix2):
    return self.elements == matrix2.elements
  def __rmul__(self, scalar):
    return self.scalar_multiply(scalar)
  def __pow__(self, num):
    return self.exponent(num)

  def copy(self):
    copied_elements = [[entry for entry in row] for row in self.elements]
    return Matrix(copied_elements)
  
  def add(self, matrix2):
    output_elements = [[0 for x in range(self.num_rows)] for y in range(self.num_cols)]
    mat2_ele = matrix2.elements
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        output_elements[i][j] = self.elements[i][j] + mat2_ele[i][j]
    return Matrix(output_elements)
  
  def subtract(self, matrix2):
    output_elements = [[0 for x in range(self.num_rows)] for y in range(self.num_cols)]
    mat2_ele = matrix2.elements
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        output_elements[i][j] = self.elements[i][j] - mat2_ele[i][j]
    return Matrix(output_elements)

  def scalar_multiply(self, scalar):
    output_elements = [[0 for x in range(self.num_rows)] for y in range(self.num_cols)]
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        output_elements[i][j] = round(self.elements[i][j] * scalar, 5)
    return Matrix(output_elements)

  def matrix_multiply(self, matrix2):
    output_elements = [[0 for x in range(matrix2.num_cols)] for y in range(self.num_rows)]
    mat2_ele = matrix2.elements
    for i in range(len(output_elements)):
      for j in range(len(output_elements[i])):
        element_sum = 0  
        for k in range(self.num_cols):
          element_sum += self.elements[i][k]*mat2_ele[k][j]
        output_elements[i][j] = element_sum 
    return Matrix(output_elements)

  def transpose(self):
    output_elements = [[0 for x in range(self.num_rows)] for y in range(self.num_cols)]
    for i in range(self.num_cols):
      for j in range(self.num_rows):
        output_elements[i][j] = self.elements[j][i]
    return Matrix(output_elements)

  def is_equal(self, matrix2):
    mat2_ele = matrix2.elements
    equality_check = True
    for i in range(len(self.elements)):
      for j in range(len(self.elements[i])):
        if self.elements[i][j] != mat2_ele[i][j]:
          equality_check = False
    return equality_check

  def non_zero_num(self, row_index):
    for i in range(self.num_cols):
      if self.elements[row_index][i] != 0:
        return self.elements[row_index][i]

  def non_zero_index(self, row_index):
    for i in range(self.num_cols):
      if self.elements[row_index][i] != 0:
        return i

  def get_pivot_row(self, column_index): 
    for row in range(len(self.elements)):
      zeros = False
      for value in range(column_index):
        if self.elements[row][value] != 0:
          zeros = True
      if zeros == False and self.elements[row][column_index] != 0:
        return row

  def swap_rows(self, row_index1, row_index2):
    result = self.copy()
    result.elements[row_index1], result.elements[row_index2] = result.elements[row_index2], result.elements[row_index1]
    return result
  
  def normalize_row(self, row_index):
    result = self.copy()
    col_num = result.non_zero_num(row_index)
    for i in range(len(result.elements[row_index])):
      result.elements[row_index][i] = result.elements[row_index][i]/col_num
    return result

  def clear_below(self, row_index):
    result = self.copy()
    col_index = result.non_zero_index(row_index)
    col_num = result.non_zero_num(col_index)
    for row in result.elements[row_index+1:]:
      scalar = row[col_index]/result.elements[row_index][col_index]
      for num in range(result.num_cols):
        row[num] -= scalar*result.elements[row_index][num]
    return result

  def clear_above(self, row_index):
    result = self.copy()
    col_index = result.non_zero_index(row_index)
    col_num = result.non_zero_num(col_index)
    for row in result.elements[:row_index]:
      scalar = row[col_index]/result.elements[row_index][col_index]
      for num in range(result.num_cols):
        row[num] -= scalar*result.elements[row_index][num]
    return result

  def rref(self):
    result = self.copy()
    row_index = 0
    for col_index in range(result.num_cols):
      pivot_row = result.get_pivot_row(col_index)
      if pivot_row != None:
        if pivot_row != row_index:
          result = result.swap_rows(pivot_row, row_index)
        result = result.normalize_row(row_index)
        result = result.clear_below(row_index)
        result = result.clear_above(row_index)
        row_index += 1
    return result
  
  def augment(self, other_matrix):
    matrix1 = self.elements
    matrix2 = other_matrix.elements
    return Matrix([a + b for a, b in zip(matrix1, matrix2)])
  
  def get_rows(self, row_nums):
    matrix = self.elements
    rows = []
    for row_index in row_nums:
      rows.append(matrix[row_index])
    return Matrix(rows)
  
  def get_columns(self, col_nums):
    cols = []
    matrix = self.elements
    for row in matrix:
      row_list = []
      for col_index in col_nums:
        row_list.append(row[col_index])
      cols.append(row_list)
    return Matrix(cols)

  def inverse(self):
    identity = Matrix([[int(x == y) for x in range(self.num_cols)] for y in range(self.num_rows)])
    mat1 = self.augment(identity)
    mat1 = mat1.rref()
    left_mat = mat1.get_columns([num for num in range(self.num_cols)])
    inverse_mat = mat1.get_columns([num for num in range(self.num_cols, 2*self.num_cols)])
    if self.num_cols != self.num_rows:
      return 'Error: cannot invert a non-square matrix'
    if left_mat.elements != identity.elements:
      return 'Error: cannot invert a singular matrix'
    return inverse_mat
  
  def determinant(self):
    result = self.copy()
    row_index = 0
    multiplied_nums = 1
    row_swaps = 0
    for col_index in range(result.num_cols):
      pivot_row = result.get_pivot_row(col_index)
      if pivot_row != None:
        if pivot_row != row_index:
          result = result.swap_rows(pivot_row, row_index)
          row_swaps += 1
        col_num = result.non_zero_num(row_index)
        for i in range(len(result.elements[row_index])):
          result.elements[row_index][i] = result.elements[row_index][i]/col_num
          multiplied_nums *= (result.elements[row_index][i]/len(result.elements[row_index]))

        result = result.clear_below(row_index)
        result = result.clear_above(row_index)
        row_index += 1
    return multiplied_nums*(-1)**row_swaps
  
  def exponent(self, num):
    mat = self.copy()
    matrix = self.copy()
    for i in range(num-1):
      matrix = matrix.matrix_multiply(mat)
    return matrix

  def cofactor_helper(self, row_num, col_num):
    mat_2 = self.copy()
    row = []
    col = []
    for num in range(mat_2.num_rows):
      if num != row_num:
        row.append(num)
    for num in range(mat_2.num_cols):
      if num != col_num:
        col.append(num)
    mat_2 = mat_2.get_rows(row)
    mat_2 = mat_2.get_columns(col)
    return mat_2

  def cofactor_method_determinant(self):
    mat = self.copy()
    mat_cols = mat.num_cols
    mat_rows = mat.num_rows
    determinant = 0
    if mat_cols == mat_rows:
      if 1 < mat_cols:
        for col_num in range(mat_cols):
          mat_2 = mat.cofactor_helper(0, col_num)
          determinant += ((-1)**col_num)*mat.elements[0][col_num]*mat_2.cofactor_method_determinant()
      else:
        return mat.elements[0][0]
    else:
      return 'Error: cannot take determinant of a non-square matrix'
    return determinant
