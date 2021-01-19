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