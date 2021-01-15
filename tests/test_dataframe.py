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

# print('testing method "select rows where..."')
# assert df.select_rows_where(lambda row: len(row['firstname']) >= len(
#   row['lastname']) and row['age'] > 10).to_array() == [['Charles', 'Trapp', 17]]
# print('passed')



path_to_datasets = '/home/runner/machine-learning/datasets/'
filename = 'airtravel.csv' 
filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath, header=True)
print('testing csv...')
assert df.columns == ['"Month"', '"1958"', '"1959"', '"1960"']
assert df.to_array() == [['"JAN"',  '340',  '360',  '417'],
  ['"FEB"',  '318',  '342',  '391'],
  ['"MAR"',  '362',  '406',  '419'],
  ['"APR"',  '348',  '396',  '461'],
  ['"MAY"',  '363',  '420',  '472'],
  ['"JUN"',  '435',  '472',  '535'],
  ['"JUL"',  '491',  '548',  '622'],
  ['"AUG"',  '505',  '559',  '606'],
  ['"SEP"',  '404',  '463',  '508'],
  ['"OCT"',  '359',  '407',  '461'],
  ['"NOV"',  '310',  '362',  '390'],
  ['"DEC"',  '337',  '405',  '432']]
print('passed')