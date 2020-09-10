import sys
sys.path.append('src')
from matrix import Matrix


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
assert G.elements == [[7,-3],[10,-4]], 'failed'
print('passed')
