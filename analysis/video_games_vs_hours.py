import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

df = DataFrame.from_array([
  (10, 0.05),
  (100, 0.35),
  (1000, 0.95)],
  columns = ['Hours Played', 'Chance of Winning'])

regressor = LogisticRegressor(df, dependent_variable='Chance of Winning', upper_bound = 1)

print(regressor.coefficients)

print(regressor.predict({'Hours Played': 500}))
print(regressor.predict({'Hours Played': 410.28988}))
