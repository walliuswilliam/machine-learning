import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['x','y']
)

log_reg = LogisticRegressor(df, dependent_variable = 'y', upper_bound = 1)

print('printing coefficients...')
print(log_reg.coefficients)
print('passed')

print('\ntesting predict...')
assert round(log_reg.predict({'x': 5}), 3) == 0.777, log_reg.predict({'x': 5})
print('passed')

