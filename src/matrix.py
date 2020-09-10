class Matrix:
  def __init__(self, elements):
    self.elements = elements
  
  def copy(self):
    return self
  
  def add(self, matrix2):
    mat2_ele = matrix2.elements
    output_elements = [[self.elements[0][0] + mat2_ele[0][0], self.elements[0][1] + mat2_ele [0][1]], [self.elements[1][0] + mat2_ele[1][0], self.elements[1][1] + mat2_ele[1][1]]]
    return Matrix(output_elements)
  
  def subtract(self, matrix2):
    mat2_ele = matrix2.elements
    output_elements = [[self.elements[0][0] - mat2_ele[0][0], self.elements[0][1] - mat2_ele[0][1]], [self.elements[1][0] - mat2_ele[1][0], self.elements[1][1] - mat2_ele[1][1]]]
    return Matrix(output_elements)

  def scalar_multiply(self, scalar):
    output_elements = [[self.elements[0][0] * scalar, self.elements[0][1] * scalar], [self.elements[1][0] * scalar, self.elements[1][1] * scalar]]
    return Matrix(output_elements)

  def matrix_multiply(self, matrix2):
    mat2_ele = matrix2.elements
    a = self.elements[0][0]
    b = self.elements[0][1]
    c = self.elements[1][0]
    d = self.elements[1][1]
    e = mat2_ele[0][0]
    f = mat2_ele[0][1]
    g = mat2_ele[1][0]
    h = mat2_ele[1][1]
    output_elements = [[(a*e+b*g), (a*f+b*h)], [(c*e+d*g),(c*f+d*h)]]
    return Matrix(output_elements)
    
    






  


# A = Matrix([[1,3], [2,4]])

# B = Matrix([[2,3], [234]])

# mat1 = [[a, b], (c, d)]  mat2 = [[e, f], (g, h)]

# [[(a*e+b*g), (a*f+b*h)], [(c*e+d*g),(c*f+d*h)]]

# a  b    e  f
# c  d    g  h

# e  f
# g  h


#   copy, add, subtract, scalar_multiply, matix_multiply

#   output_elements = [[self.elements[0][0]*mat2_ele[0][0]+self.elements[0][1]*mat2_ele[1][0], self.elements[0][0]*mat2_ele[0][1]+self.elements[0][1]*mat2_ele[1][1]], [[[self.elements[1][0]*mat2_ele[0][0]+self.elements[1][1]*mat2_ele[1][0]], [self.elements[1][0] - mat2_ele[1][0], self.elements[1][1] - mat2_ele[1][1]]]]]