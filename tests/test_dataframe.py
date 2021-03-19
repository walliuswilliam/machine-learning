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
df2 = df1.select(['Sarah', 'Pete'])
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



# path_to_datasets = '/home/runner/machine-learning/datasets/'
# filename = 'airtravel.csv' 
# filepath = path_to_datasets + filename
# df = DataFrame.from_csv(filepath, header=True)
# print('testing csv...')
# assert df.columns == ['"Month"', '"1958"', '"1959"', '"1960"']
# assert df.to_array() == [['"JAN"',  '340',  '360',  '417'],
#   ['"FEB"',  '318',  '342',  '391'],
#   ['"MAR"',  '362',  '406',  '419'],
#   ['"APR"',  '348',  '396',  '461'],
#   ['"MAY"',  '363',  '420',  '472'],
#   ['"JUN"',  '435',  '472',  '535'],
#   ['"JUL"',  '491',  '548',  '622'],
#   ['"AUG"',  '505',  '559',  '606'],
#   ['"SEP"',  '404',  '463',  '508'],
#   ['"OCT"',  '359',  '407',  '461'],
#   ['"NOV"',  '310',  '362',  '390'],
#   ['"DEC"',  '337',  '405',  '432']]
# print('passed')


df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)

df = df.create_dummy_variables('condiments')

print('testing columns...')
assert df.columns == ['beef', 'pb', 'mayo', 'jelly', 'rating']
print('passed')

print('testing array data...')
assert df.to_array() == [
  [0, 0, 0, 0, 1],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 4],
  [0, 0, 1, 1, 0],
  [5, 0, 0, 0, 4],
  [5, 0, 1, 0, 8],
  [5, 0, 0, 1, 1],
  [5, 0, 1, 1, 0],
  [0, 5, 0, 0, 5],
  [0, 5, 1, 0, 0],
  [0, 5, 0, 1, 9],
  [0, 5, 1, 1, 0],
  [5, 5, 0, 0, 0],
  [5, 5, 1, 0, 0],
  [5, 5, 0, 1, 0],
  [5, 5, 1, 1, 0]]
print('passed')


print('testing SQL methods...')

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

assert df.select(['firstname','age']).to_array() == [
  ['Kevin', 5],
  ['Charles', 17],
  ['Anna', 13],
  ['Sylvia', 9]]

assert df.where(lambda row: row['age'] > 10).to_array() == [
  ['Charles', 'Trapp', 17],
  ['Anna', 'Smith', 13]]

assert df.order_by('firstname').to_array() == [
  ['Anna', 'Smith', 13],
  ['Charles', 'Trapp', 17],
  ['Kevin', 'Fray', 5],
  ['Sylvia', 'Mendez', 9]]

assert df.order_by('firstname', ascending=False).to_array() == [
  ['Sylvia', 'Mendez', 9],
['Kevin', 'Fray', 5],
['Charles', 'Trapp', 17],
['Anna', 'Smith', 13]]

assert df.select(['firstname','age']).where(lambda row: row['age'] > 10).order_by('age').to_array() == [
  ['Anna', 13],
  ['Charles', 17]]



df = DataFrame.from_array(
    [
        ['Kevin Fray', 52, 100],
        ['Charles Trapp', 52, 75],
        ['Anna Smith', 52, 50],
        ['Sylvia Mendez', 52, 100],
        ['Kevin Fray', 53, 80],
        ['Charles Trapp', 53, 95],
        ['Anna Smith', 53, 70],
        ['Sylvia Mendez', 53, 90],
        ['Anna Smith', 54, 90],
        ['Sylvia Mendez', 54, 80],
    ],
    columns = ['name', 'assignmentId', 'score']
)

assert df.group_by('name').to_array() == [
    ['Kevin Fray', [52, 53], [100, 80]],
    ['Charles Trapp', [52, 53], [75, 95]],
    ['Anna Smith', [52, 53, 54], [50, 70, 90]],
    ['Sylvia Mendez', [52, 53, 54], [100, 90, 80]]
], df.group_by('name').to_array()



assert df.group_by('name').aggregate('score', 'count').to_array() == [
    ['Kevin Fray', [52, 53], 2],
    ['Charles Trapp', [52, 53], 2],
    ['Anna Smith', [52, 53, 54], 3],
    ['Sylvia Mendez', [52, 53, 54], 3],
]

assert df.group_by('name').aggregate('score', 'max').to_array() == [
    ['Kevin Fray', [52, 53], 100],
    ['Charles Trapp', [52, 53], 95],
    ['Anna Smith', [52, 53, 54], 90],
    ['Sylvia Mendez', [52, 53, 54], 100],
]

assert df.group_by('name').aggregate('score', 'min').to_array() == [
    ['Kevin Fray', [52, 53], 80],
    ['Charles Trapp', [52, 53], 75],
    ['Anna Smith', [52, 53, 54], 50],
    ['Sylvia Mendez', [52, 53, 54], 80],
]

assert df.group_by('name').aggregate('score', 'sum').to_array() == [
    ['Kevin Fray', [52, 53], 180],
    ['Charles Trapp', [52, 53], 170],
    ['Anna Smith', [52, 53, 54], 210],
    ['Sylvia Mendez', [52, 53, 54], 270],
]

assert df.group_by('name').aggregate('score', 'avg').to_array() == [
    ['Kevin Fray', [52, 53], 90],
    ['Charles Trapp', [52, 53], 85],
    ['Anna Smith', [52, 53, 54], 70],
    ['Sylvia Mendez', [52, 53, 54], 90],
]

print('passed')



print('testing initial query method...')

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

assert df.query('SELECT firstname, age').to_array() == [
  ['Kevin', 5],
  ['Charles', 17],
  ['Anna', 13],
  ['Sylvia', 9]]

print('passed')