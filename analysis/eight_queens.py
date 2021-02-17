import random

def show_board(locations):
  board = ''
  for num in range(8):
    board += '........\n'
  for point in range(len(locations)):
    point_on_board = locations[point][0]*9+locations[point][1]
    board = board[:point_on_board] + str(point) + board[point_on_board+1:]
    
    #adds spaces between the values
    separator = [char for char in board] 
    separator.insert(0,'')
    board_final = '  '.join(separator)
  return board_final

def col_row_checker(coords, locations):
  cost = 0
  for point in range(len(locations)):
    if coords != locations[point]:
      if coords[1] == locations[point][1]:
        cost += 1
      if coords[0] == locations[point][0]:
        cost += 1
  return cost/2

def diagonal_checker(locations):
  cost = 0
  for point_1 in locations:
    for point_2 in locations:
      if (point_1[0]-point_2[0]) != 0:
        slope = (point_1[1]-point_2[1])/(point_1[0]-point_2[0])
        if slope == 1 or slope == -1:
          cost += 1
  return cost/2

def calc_cost(locations):
  total_cost = 0
  for point in locations:
    total_cost += col_row_checker(point, locations)
  total_cost += diagonal_checker(locations)
  
  for point_index_1 in range(len(locations)):
    for point_index_2 in range(len(locations)):
      if point_index_1 != point_index_2:
        if locations[point_index_1][0] == locations[point_index_2][0] and locations[point_index_1][1] == locations[point_index_1][1]:
          total_cost += 1

  return total_cost


def rand_point():
  return (random.randint(0,7), random.randint(0,7))

def random_optimizer(n):
  min_location = []
  min_cost = 10000000
  for num in range(n):
    test_location = [rand_point() for num in range(8)]
    test_cost = calc_cost(test_location)
    if test_cost < min_cost:
      min_location = test_location
      min_cost = test_cost
  return  {'locations': min_location, 'cost': min_cost}


if __name__ == "__main__":
  print('showing board...')
  locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
  print(show_board(locations))

  print('\ncalculating cost...')
  assert calc_cost(locations) == 10
  print('passed')

  print('\ntesting random_optimizer on n_vals...')
  n_vals = [10, 50, 100, 500, 1000]
  for n in n_vals:
    print('n =', n, ':', random_optimizer(n))

