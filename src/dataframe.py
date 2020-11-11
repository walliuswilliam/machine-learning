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
    temp_dict = {key:dictionary[key] for key in columns}
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
    data_dict = {columns[key]:[data for data in arr[i for i in range(len(arr))][key]]}
    return data_dict

    





  

data_dict = {
  'Pete': [1, 0, 1, 0],
  'John': [2, 1, 0, 2],
  'Sarah': [3, 1, 4, 0]
  }

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])

print('testing attribute "data_dict"...')
assert df1.data_dict == {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}
print('passed')

print('testing attribute "columns"...')
assert df1.columns == ['Pete', 'John', 'Sarah']
print('passed')

print('testing method "to_array"...')
assert df1.to_array() == [[1, 2, 3],
 [0, 1, 1],
 [1, 0, 4],
 [0, 2, 0]]
print('passed')

print('testing method "select_columns"...')
df2 = df1.select_columns(['Sarah', 'Pete'])
print('passed')

print('testing method "to_array"...')
assert df2.to_array() == [[3, 1],
 [1, 0],
 [4, 1],
 [0, 0]]
print('passed')

print('testing attribute "columns"...')
assert df2.columns == ['Sarah', 'Pete']
print('passed')

print('testing method "select_rows"...')
df3 = df1.select_rows([1,3])
print('passed')

print('testing method "to_array"...')
assert df3.to_array() == [[0, 1, 1], [0, 2, 0]], df3.to_array()
print('passed')


data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

print('testing method "apply"...')
df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])
df2 = df1.apply('John', lambda x: 7 * x)
assert df2.data_dict == {
    'Pete': [1, 0, 1, 0],
    'John': [14, 7, 0, 14],
    'Sarah': [3, 1, 4, 0]
}
print('passed')

columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5],
           ['Charles', 'Trapp', 17],
           ['Anna', 'Smith', 13],
           ['Sylvia', 'Mendez', 9]]
df = DataFrame.from_array(arr, columns)