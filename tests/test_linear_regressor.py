import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from dataframe import DataFrame

# df = DataFrame.from_array(
#     [[1,0.2],
#      [2,0.25],
#      [3,0.5]],
#     columns = ['hours worked', 'progress']
# )
# regressor = LinearRegressor(df, dependent_variable='progress')
# print('testing attribute "coefficients"...')
# assert regressor.coefficients == [0.01667, 0.15] # meaning that the model is progress = 0.01667 + 0.15 * (hours worked)
# # these coefficients are rounded, but you should not round except for
# # in your assert statement
# print('passed')

# print('testing method "predict"...')
# assert regressor.predict({'hours worked': 4}) == 0.61667, regressor.predict({'hours worked': 4})
# print('passed')

print("___ASSIGNMENT 40____")

df = DataFrame.from_array(
    [[0, 0, 0.1],
     [1, 0, 0.2],
     [0, 2, 0.5],
     [4,5,0.6]],
    columns = ['scoops of chocolate', 'scoops of vanilla', 'taste rating']
)

regressor = LinearRegressor(df, dependent_variable='taste rating')

print('testing attribute "coefficients"...')
assert {k:round(v,8) for k,v in regressor.coefficients.items()} == {'constant': 0.19252336, 'scoops of chocolate': -0.05981308,'scoops of vanilla': 0.13271028}, {k:round(v,8) for k,v in regressor.coefficients.items()}
print('passed')

print('testing method "predict"...')
assert round(regressor.predict({'scoops of chocolate': 2, 'scoops of vanilla': 3}), 8) == 0.47102804


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
    columns = ['beef', 'pb', 'condiments', 'rating'])

df = df.create_dummy_variables('condiments')

df = df.create_interaction_terms('beef', 'pb')
df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo',)
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')

linear_regressor = LinearRegressor(df, dependent_variable='rating')


print('testing observation 1...')
observation = {'beef': 8, 'mayo': 1}
assert round(linear_regressor.predict(observation), 2) == 11.34
print('passed')

print('testing observation 2...')
# test 4 tbsp of pb + 8 slices of beef + mayo
observation = {'beef': 8, 'pb': 4, 'mayo': 1}
assert round(linear_regressor.predict(observation), 2) == 3.62
print('passed')

print('testing observation 3...')
# test 8 slices of beef + mayo + jelly
observation = {'beef': 8, 'mayo': 1, 'jelly': 1}
assert round(linear_regressor.predict(observation), 2) == 2.79
print('passed')
