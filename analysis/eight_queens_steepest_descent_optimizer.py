import sys
sys.path.append('analysis')
from eight_queens import *


def steepest_descent_optimizer(n):
  random_board = random_optimizer(100)
  print('initial board', random_board)
  optimised_array = random_board['locations']

  for iteration in range(n):
    test_array = optimised_array.copy()
    reset_array = test_array.copy()

    for queen_index in range(len(optimised_array)):
      if 0 <= test_array[queen_index][0]+1 < 8:
        test_array[queen_index] = (test_array[queen_index][0]+1, test_array[queen_index][1])
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array
      
      test_array = reset_array.copy()
      if 0 <= test_array[queen_index][0]-1 < 8:
        test_array[queen_index] = (test_array[queen_index][0]-1, test_array[queen_index][1])
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array

      test_array = reset_array.copy()
      
      if 0 <= test_array[queen_index][1]+1 < 8:
        test_array[queen_index] = (test_array[queen_index][0], test_array[queen_index][1]+1)
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array

      test_array = reset_array.copy()
      
      if 0 <= test_array[queen_index][1]-1 < 8:
        test_array[queen_index] = (test_array[queen_index][0], test_array[queen_index][1]-1)
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array

      test_array = reset_array.copy()

      if 0 <= test_array[queen_index][0]+1 < 8 and 0 <= test_array[queen_index][1]+1 < 8:
        test_array[queen_index] = (test_array[queen_index][0]+1, test_array[queen_index][1]+1)
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array

      test_array = reset_array.copy()
      
      if 0 <= test_array[queen_index][0]-1 < 8 and 0 <= test_array[queen_index][1]-1 < 8:
        test_array[queen_index] = (test_array[queen_index][0]-1, test_array[queen_index][1]-1)
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array

      test_array = reset_array.copy()
      
      if 0 <= test_array[queen_index][0]+1 < 8 and 0 <= test_array[queen_index][1]-1 < 8:
        test_array[queen_index] = (test_array[queen_index][0]+1, test_array[queen_index][1]-1)
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array

      test_array = reset_array.copy()
      
      if 0 <= test_array[queen_index][0]-1 < 8 and 0 <= test_array[queen_index][1]+1 < 8:
        test_array[queen_index] = (test_array[queen_index][0]-1, test_array[queen_index][1]+1)
        if calc_cost(test_array) < calc_cost(optimised_array):
          optimised_array = test_array

      test_array = reset_array.copy()

  return {'locations': optimised_array, 'cost': calc_cost(optimised_array)}
        

for n in [10,50,100,500,1000]:
  print('n =', n, ':')
  print('optimized board', steepest_descent_optimizer(n), '\n')