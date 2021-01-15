def show_board(locations):
  board = '........\n........\n........\n........\n........\n........\n........\n........'
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
  return total_cost
  

locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
print(show_board(locations))

print(calc_cost(locations))