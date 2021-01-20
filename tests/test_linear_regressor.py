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
assert regressor.predict({'scoops of chocolate': 2, 'scoops of vanilla': 3}) == 0.47102804
print('passed')
