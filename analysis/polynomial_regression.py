import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

df = [(0.0, 4.0),
      (0.2, 8.9),
      (0.4, 17.2),
      (0.6, 28.3),
      (0.8, 41.6),
      (1.0, 56.5),
      (1.2, 72.4),
      (1.4, 88.7),
      (1.6, 104.8),
      (1.8, 120.1),
      (2.0, 134.0),
      (2.2, 145.9),
      (2.4, 155.2),
      (2.6, 161.3),
      (2.8, 163.6),
      (3.0, 161.5),
      (3.2, 154.4),
      (3.4, 141.7),
      (3.6, 122.8),
      (3.8, 97.1),
      (4.0, 64.0),
      (4.2, 22.9),
      (4.4, -26.8),
      (4.6, -85.7),
      (4.8, -154.4)]

for point_index in range(len(df)):
  x = df[point_index][0]
  df[point_index] = (x, x**2, x**3, df[point_index][1])

print(df)

df = DataFrame.from_array(df, columns = ['x', 'x^2', 'x^3', 'y'])

regressor = LinearRegressor(df, dependent_variable='y')

print(regressor.coefficients)
