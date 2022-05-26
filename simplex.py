class Simplex:
    def __init__(self, matrix):
        self.matrix = matrix
        self.max = self.find_max()

    def get_col(self, i=-1):
        return [row[i] for row in self.matrix]

    def choose_col(self): #returns index
        last_row = self.matrix[-1]
        return last_row.index((max(last_row)))

    def choose_row(self, chosen_col): #returns index
        const = self.get_col()[:-1]
        col = self.get_col(i=chosen_col)[:-1]
        row_idx = 0
        
        for i in range(len(const)):
            if 0 < const[i]/col[i] < const[row_idx]/col[row_idx]:
                row_idx = i
        return row_idx

    def reduce_row(self, row_idx, col_idx):
        row = self.matrix[row_idx]
        self.matrix[row_idx] = [i/row[col_idx] for i in row]

    def clear_above_and_below(self, col_idx, row_idx):
        for row_i, row in enumerate(self.matrix):
            temp_row = []
            if row_i != row_idx:
                for col_i, element in enumerate(row):
                    temp_row.append(element-row[col_idx]*self.matrix[row_idx][col_i])
                self.matrix[row_i] = temp_row

    def find_max(self):
        while max(self.matrix[-1]) > 0:
            col = self.choose_col()
            row = self.choose_row(col)
            self.reduce_row(row, col)
            self.clear_above_and_below(col, row)
        return -self.matrix[-1][-1]

    def print_coeffs(self):
        coeffs = {'x1':None,'x2':None,'x3':None}
        for row in self.matrix:
            if row[0] == 1:
                coeffs['x1'] = row[-1]
            if row[1] == 1:
                coeffs['x2'] = row[-1]
            if row[2] == 1:
                coeffs['x3'] = row[-1]
        print(coeffs)



matrix = [[3,2,5,1,0,0,0,55],[2,1,1,0,1,0,0,26],[1,1,3,0,0,1,0,30],[5,2,4,0,0,0,1,57],[20,10,15,0,0,0,0,0]]
s = Simplex(matrix)
s.print_coeffs()
print('max', s.max, '\n')

matrix = [[2,1,1,1,0,0,14],[4,2,3,0,1,0,28],[2,5,5,0,0,1,30],[1,2,1,0,0,0,0]]
s = Simplex(matrix)
s.print_coeffs()
print('max', s.max)
