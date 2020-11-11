import sys
sys.path.append('src')
from dataframe import DataFrame


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