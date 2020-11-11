import sys
sys.path.append('src')
from matrix import Matrix

print('--------------Assignment 6----------------')
A = Matrix([[1,3], [2,4]])
print("getting elements of A...")
assert A.elements == [[1,3], [2,4]], 'failed'
print('passed')

B = A.copy()
A = 'resetting A to a string'
print('Testing method "copy"...')
assert B.elements == [[1,3], [2,4]], 'failed'
print('passed')

C = Matrix([[1,0], [2,-1]])
D = B.add(C)
print('Testing method "add"...')
assert D.elements == [[2,3], [4,3]], 'failed'
print('passed')

E = B.subtract(C)
print('Testing method "subtract"...')
assert E.elements == [[0,3], [0,5]], 'failed'
print('passed')

F = B.scalar_multiply(2)
print('Testing method "scalar_multiply"...')
assert F.elements == [[2,6], [4,8]] ,'failed'
print('passed')

G = B.matrix_multiply(C)
print('Testing method "matrix_multiply"...')
assert G.elements == [[7,-3],[10,-4]], G.elements
print('passed')
print('')
print('')
print('--------------Assignment 7----------------')


A = 'resetting A to a string'

print('getting number of rows and columns...')
A = Matrix([[1,0,2,0,3],[0,4,0,5,0],[6,0,7,0,8],[-1,-2,-3,-4,-5]])
assert (A.num_rows, A.num_cols) == (4, 5), 'failed'
print('passed')

print('Testing method "transpose"...')
A_t = A.transpose()
assert A_t.elements == [[ 1,  0,  6, -1], [ 0,  4,  0, -2],
  [ 2,  0,  7, -3], [ 0,  5,  0, -4], [ 3,  0,  8, -5]], 'failed'
print('passed')

print('Testing method "matrix multiply"...')
B = A_t.matrix_multiply(A)
assert B.elements == [[38,  2, 47,  4, 56],[ 2, 20,  6, 28, 10],[47,  6, 62, 12, 77],
  [ 4, 28, 12, 41, 20],[56, 10, 77, 20, 98]], B.elements
print('passed')

print('Testing method "scalar multiply"...')
C = B.scalar_multiply(0.1)
assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6],[ .2, 2.0,  .6, 2.8, 1.0], 
  [4.7,  .6, 6.2, 1.2, 7.7],[ .4, 2.8, 1.2, 4.1, 2.0],[5.6, 1.0, 7.7, 2.0, 9.8]], 'failed'
print('passed')

print('Testing method "subtract"...')
D = B.subtract(C)
assert D.elements == [[34.2,  1.8, 42.3,  3.6, 50.4], [ 1.8, 18. ,  5.4, 25.2,  9. ],
  [42.3,  5.4, 55.8, 10.8, 69.3], [ 3.6, 25.2, 10.8, 36.9, 18. ], 
  [50.4,  9. , 69.3, 18. , 88.2]], 'failed'
print('passed')

print('Testing method "add"...')
E = D.add(C)
assert E.elements == [[38,  2, 47,  4, 56], [ 2, 20,  6, 28, 10], [47,  6, 62, 12, 77],
  [ 4, 28, 12, 41, 20], [56, 10, 77, 20, 98]], 'failed'
print('passed')

print('Testing method "is equal"...')
assert (E.is_equal(B), E.is_equal(C)) == (True, False), 'failed'
print('passed')
print('')
print('')
print('--------------Assignment 8----------------')

A = 'resetting A to a string'
print('Testing method "pivot row"...')
A = Matrix(elements = [[0, 1, 2],[3, 6, 9],[2, 6, 8]])
assert A.get_pivot_row(0) == 1, A.get_pivot_row(0)
print('passed')

print('Testing method "swap rows"...')
A = A.swap_rows(0,1)
assert A.elements == [[3, 6, 9],[0, 1, 2],[2, 6, 8]], 'failed'
print('passed')

print('Testing method "normalize row"...')
A = A.normalize_row(0)
assert A.elements == [[1, 2, 3],[0, 1, 2],[2, 6, 8]], A.normalize_row(0)
print('passed')

print('Testing method "clear below"...')
A = A.clear_below(0)
assert A.elements == [[1, 2, 3],[0, 1, 2],[0, 2, 2]]
print('passed')

print('Testing method "pivot row"...')
assert A.get_pivot_row(1) == 1, A.get_pivot_row(1)
print('passed')

print('Testing method "normalize row"...')
A = A.normalize_row(1)
assert A.elements == [[1, 2, 3],[0, 1, 2],[0, 2, 2]]
print('passed')

print('Testing method "clear below"...')
A = A.clear_below(1)
assert A.elements == [[1, 2, 3],[0, 1, 2],[0, 0, -2]]
print('passed')

print('Testing method "pivot row"...')
assert A.get_pivot_row(2) == 2, 'failed'
print('passed')

print('Testing method "normalize row"...')
A = A.normalize_row(2)
assert A.elements == [[1, 2, 3],[0, 1, 2],[0, 0, 1]]
print('passed')

print('Testing method "clear above"...')
A = A.clear_above(2)
assert A.elements == [[1, 2, 0],[0, 1, 0],[0, 0, 1]]
print('passed')

print('Testing method "clear above"...')
A = A.clear_above(1)
assert A.elements == [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
print('passed')
print('')
print('')
print('--------------Assignment 11----------------')

print('testing method "rref"...')
A = Matrix([[0, 1, 2],[3, 6, 9],[2, 6, 8]])
assert A.rref().elements == [[1, 0, 0],[0, 1, 0],[0, 0, 1]], A.rref().elements
print('passed')

B = Matrix([[0, 0, -4, 0],[0, 0, 0.3, 0], [0, 2, 1, 0]])
assert B.rref().elements == [[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 0]], B.rref().elements
print("passed")


print('')
print('')
print('--------------Assignment 15----------------')
A = Matrix([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
B = Matrix([[13, 14],[15, 16],[17, 18]])

A_augmented = A.augment(B)
print('testing method "augment"...')
assert A_augmented.elements == [[1, 2, 3, 4, 13, 14],[5, 6, 7, 8, 15, 16],[
  9, 10, 11, 12, 17, 18]], A_augmented.elements
print('passed')

rows_02 = A_augmented.get_rows([0, 2])
print('testing method "get rows"...')
assert rows_02.elements == [[1, 2, 3, 4, 13, 14],[9, 10, 11, 12, 17, 18]]
print('passed')

cols_0123 = A_augmented.get_columns([0, 1, 2, 3])
print('testing method "get columns"...')
assert cols_0123.elements == [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
print('passed')

cols_45 = A_augmented.get_columns([4, 5])
print('testing method "get columns"...')
assert cols_45.elements == [[13, 14],[15, 16],[17, 18]]
print('passed')

print('')
print('')
print('--------------Assignment 17----------------')
A = Matrix([[1, 2],[3, 4]])

print('testing method inverse...')
A_inv = A.inverse()
assert A_inv.elements == [[-2,1],[1.5,-0.5]]
print('passed')

A = Matrix([[1,2,3],[1,0,-1],[0.5,0,0]])
A_inv = A.inverse()
assert A_inv.elements == [[0,0,2],[0.5,1.5,-4],[0,-1,2]]
print('passed')

A = Matrix([[1, 2, 3, 0],[1, 0, 1, 0],[0, 1, 0, 0]])
A_inv = A.inverse()
assert A_inv == 'Error: cannot invert a non-square matrix'
print('passed')

# A = Matrix([[1, 2, 3],[3, 2, 1],[1, 1, 1]])
# A_inv = A.inverse()
# assert A_inv == 'Error: cannot invert a singular matrix'
# print('passed')

print('')
print('')
print('--------------Assignment 21----------------')
# A = Matrix(elements = [[1,2],[3,4]])
# ans = A.determinant()
# assert round(ans,6) == -2, round(ans,6)

# A = Matrix(elements = [[1,2,0.5],[3,4,-1],[8,7,-2]])
# ans = A.determinant()
# assert round(ans,6) == -10.5

# A = Matrix(elements = [[1,2,0.5,0,1,0],[3,4,-1,1,0,1],[8,7,-2,1,1,1],[-1,1,0,1,0,1],[0,0.35,0,-5,1,1],[1,1,1,1,1,0]])
# ans = A.determinant()
# assert round(ans,6) == -37.3

# # A = Matrix(elements = [[1,2,0.5,0,1,0],[3,4,-1,1,0,1],[8,7,-2,1,1,1],[-1,1,0,1,0,1],[0,0.35,0,-5,1,1],[1,1,1,1,1,0],[2,3,1.5,1,2,0]])
# # ans = A.determinant()
# # assert ans == 'Error: cannot take determinant of a non-square matrix'

# A = Matrix(elements = [[1,2,0.5,0,1,0,1],[3,4,-1,1,0,1,0],[8,7,-2,1,1,1,0],[-1,1,0,1,0,1,0],[0,0.35,0,-5,1,1,0],[1,1,1,1,1,0,0],[2,3,1.5,1,2,0,1]])
# ans = A.determinant()
# assert round(ans,6) == 0

print('')
print('')
print('--------------Assignment 26----------------')
A = Matrix([[1, 1, 0],[2, -1, 0],[0, 0, 3]])
print('testing method exponent...')
assert A.exponent(3).elements == [[3, 3, 0],[6, -3, 0], [0, 0, 27]], A.exponent(3).elements
print('passed')

print('--OVERLOADING--')
A = Matrix([[1,0,2,0,3],[0,4,0,5,0],[6,0,7,0,8],[-1,-2,-3,-4,-5]])

print('testing method transpose...')
A_t = A.transpose()
assert A_t.elements == [[1,0,6,-1],[0,4,0,-2],[2,0,7,-3],[0,5,0,-4],[3,0,8,-5]]
print('passed')

print('testing overload matmul...')
B = A_t @ A
assert B.elements == [[38,  2, 47,  4, 56],
 [ 2, 20,  6, 28, 10],
 [47,  6, 62, 12, 77],
 [ 4, 28, 12, 41, 20],
 [56, 10, 77, 20, 98]]
print('passed')

print('testing overload mul...')
C = B * 0.1
assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6],
 [ .2, 2.0,  .6, 2.8, 1.0],
 [4.7,  .6, 6.2, 1.2, 7.7],
 [ .4, 2.8, 1.2, 4.1, 2.0],
 [5.6, 1.0, 7.7, 2.0, 9.8]]
print('passed')

print('testing overload sub...')
D = B - C
assert D.elements == [[34.2,  1.8, 42.3,  3.6, 50.4],
 [ 1.8, 18. ,  5.4, 25.2,  9. ],
 [42.3,  5.4, 55.8, 10.8, 69.3],
 [ 3.6, 25.2, 10.8, 36.9, 18. ],
 [50.4,  9. , 69.3, 18. , 88.2]]
print('passed')

print('testing overload add...')
E = D + C
assert E.elements == [[38,  2, 47,  4, 56],
 [ 2, 20,  6, 28, 10],
 [47,  6, 62, 12, 77],
 [ 4, 28, 12, 41, 20],
 [56, 10, 77, 20, 98]]
print('passed')

print('testing overload eq...')
assert (E == B) == True
print('passed')

print('testing overload eq...')
assert (E == C) == False
print('passed')

print('testing method cofactor determinant...')
A = Matrix(elements = [[1,2],[3,4]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == -2, round(ans,6)
print('passed')

A = Matrix(elements = [[1,2,0.5],[3,4,-1],[8,7,-2]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == -10.5
print('passed')

A = Matrix(elements = [[1,2,0.5,0,1,0],[3,4,-1,1,0,1],[8,7,-2,1,1,1],[-1,1,0,1,0,1],[0,0.35,0,-5,1,1],[1,1,1,1,1,0]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == -37.3
print('passed')

A = Matrix(elements = [[1,2,0.5,0,1,0],[3,4,-1,1,0,1],[8,7,-2,1,1,1],[-1,1,0,1,0,1],[0,0.35,0,-5,1,1],[1,1,1,1,1,0],[2,3,1.5,1,2,0]])
ans = A.cofactor_method_determinant()
assert ans == 'Error: cannot take determinant of a non-square matrix'
print('passed')

A = Matrix(elements = [[1,2,0.5,0,1,0,1],[3,4,-1,1,0,1,0],[8,7,-2,1,1,1,0],[-1,1,0,1,0,1,0],[0,0.35,0,-5,1,1,0],[1,1,1,1,1,0,0],[2,3,1.5,1,2,0,1]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == 0
print('passed')

print('')
print('')
print('--------------Assignment 26----------------')
A = Matrix([[1, 1, 0],[2, -1, 0],[0, 0, 3]])

print('testing overload rmul...')
B = 0.1 * A
assert B.elements == [[0.1, 0.1, 0],[0.2, -0.1, 0],[0, 0, 0.3]]
print('passed')

print('testing overload pow...')
C = A**3
assert C.elements == [[3, 3, 0],[6, -3, 0],[0, 0, 27]]
print('passed')
