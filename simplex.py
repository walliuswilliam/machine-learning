def get_col(matrix, i='c'):
    if i != 'c':
        return [row[i] for row in matrix]
    else:
        return [row[-1] for row in matrix]

def choose_col(matrix):
    last_row = matrix[-1]
    return last_row.index((max(last_row)))

def choose_row(matrix, chosen_col):
    const = get_col(matrix)[:-1]
    col = get_col(matrix, chosen_col)[:-1]
    row_idx = 0
    
    for i in range(len(const)):
        if 0 < const[i]/col[i] < const[row_idx]/col[row_idx]:
            row_idx = i
    return row_idx

def reduce_row(matrix, row_idx, col_idx):
    row = matrix[row_idx]
    matrix[row_idx] = [i/row[col_idx] for i in row]
    return matrix

def clear_above_and_below(matrix, col_idx, row_idx):
    for row_i, row in enumerate(matrix):
        temp_row = []
        if row_i != row_idx:
            for col_i, element in enumerate(row):
                temp_row.append(element-row[col_idx]*matrix[row_idx][col_i])
            matrix[row_i] = temp_row
    return matrix

            
def find_max(matrix):
    while max(matrix[-1]) > 0:
        col = choose_col(matrix)
        row = choose_row(matrix, col)
        matrix = reduce_row(matrix, row, col)
        matrix = clear_above_and_below(matrix, col, row)
    return -matrix[-1][-1]
matrix = [[3,2,5,1,0,0,0,55],[2,1,1,0,1,0,0,26],[1,1,3,0,0,1,0,30],[5,2,4,0,0,0,1,57],[20,10,15,0,0,0,0,0]]

print(find_max(matrix))



# matrix = [[3,2,5,55],[2,1,1,26],[1,1,3,30],[5,2,4,57],[20,10,15,0]]

# print(get_col(matrix, i=2))
# print(choose_row(matrix, choose_col(matrix)))

# sa = SimplexAlg(matrix_rep)

# print(sa.solutions())

# matrix = [[2,1,1,14],[4,2,3,28],[2,5,5,30],[1,2,1,0]]
# sa = SimplexAlg(matrix_rep)

# print(sa.solutions())


