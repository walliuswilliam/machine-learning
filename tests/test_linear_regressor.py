import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from dataframe import DataFrame

df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['hours worked', 'progress']
)
regressor = LinearRegressor(df, dependent_variable='progress')
print('testing attribute "coefficients"...')
assert regressor.coefficients == [0.01667, 0.15] # meaning that the model is progress = 0.01667 + 0.15 * (hours worked)
# these coefficients are rounded, but you should not round except for
# in your assert statement
print('passed')

print('testing method "predict"...')
assert regressor.predict({'hours worked': 4}) == 0.61667, regressor.predict({'hours worked': 4})
print('passed')