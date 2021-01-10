class DataFrame:
  def __init__(self, data_dict, column_order):
    self.data_dict = data_dict
    self.columns = column_order
  
  def to_array(self): 
    temp_dict = self.data_dict
    col_index = 0
    col_len = len(temp_dict[self.columns[0]])
    final_array = [[0 for col in self.columns] for row in range(col_len)]
    for col in self.columns:
      for dict_index in range(len(temp_dict[col])):
        final_array[dict_index][col_index] = temp_dict[col][dict_index]
      col_index += 1
    return final_array

  def select_columns(self, columns):
    dictionary = self.data_dict
    temp_dict = {key:dictionary[key] for key in self.columns}
    final_dict = DataFrame(temp_dict, columns)
    return final_dict

  def select_rows(self, rows):
    final_dict = self.data_dict
    for key in final_dict:
      final_dict[key] = [self.data_dict[key][num] for num in rows]
    return DataFrame(final_dict, self.columns)

  def apply(self, name, funct):
    final_dict = self.data_dict
    prev_list = self.data_dict[name]
    final_dict[name] = [funct(num) for num in prev_list]
    return DataFrame(final_dict, self.columns)

  @classmethod
  def from_array(cls, arr, columns):
    data_dict = {columns[key]:[[arr[i][key] for i in range(len(arr))]] for key in range(len(columns))}
    return cls(data_dict, columns)

  def convert_row_from_array_to_dict(self, row):
    row_to_dict = {self.columns[index]:row[index] for index in range(len(row))}
    return row_to_dict
  
  def select_rows_where(self, funct):
    dict_rows = {self.columns[i]:[] for i in range(len(self.columns))}
    rows = [self.convert_row_from_array_to_dict(row_index) for row_index in self.to_array()]
    
    for row in rows:
      if funct(row):
        for key, value in row.items():
          dict_rows[key].append(value)
    return DataFrame(dict_rows, self.columns)

  def from_csv(path_to_csv, header=True):


