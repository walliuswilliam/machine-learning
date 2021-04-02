import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame
import matplotlib.pyplot as plt
# from gradient_descent import GradienDesecnt


df = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    columns = ['x', 'y'])
  
arr_01 = df.to_array().copy()
arr_001 = df.to_array().copy()
arr_0001 = df.to_array().copy()
arr_00001 = df.to_array().copy()

for row in arr_01:
  if row[1] == 0:
    row[1] = 0.1
  elif row[1] == 1:
    row[1] = 0.9

for row in arr_001:
  if row[1] == 0:
    row[1] = 0.01
  elif row[1] == 1:
    row[1] = 0.99

for row in arr_0001:
  if row[1] == 0:
    row[1] = 0.001
  elif row[1] == 1:
    row[1] = 0.999

for row in arr_00001:
  if row[1] == 0:
    row[1] = 0.0001
  elif row[1] == 1:
    row[1] = 0.9999
  



df_01 = DataFrame.from_array(arr_01, columns = ['x', 'y'])
df_001 = DataFrame.from_array(arr_001, columns = ['x', 'y'])
df_0001 = DataFrame.from_array(arr_0001, columns = ['x', 'y'])
df_00001 = DataFrame.from_array(arr_00001, columns = ['x', 'y'])

regressor_list = [LogisticRegressor(df_01, 'y', 1), LogisticRegressor(df_001, 'y', 1), LogisticRegressor(df_0001, 'y', 1), LogisticRegressor(df_00001, 'y', 1)]


plt.style.use('bmh')
for regressor in regressor_list:
  x_vals = []
  y_vals = []
  for x in range(10):
    x_vals.append(x)
    y_vals.append(regressor.predict({'x': x}))
  plt.plot(x_vals, y_vals)

plt.legend(['0.1', '0.01', '0.001', '0.0001'])
plt.title('Differences of Logistic Regressors')
plt.savefig('analysis/logistic_issues.png')


plt.clf()
plt.style.use('bmh')
x_vals = []
y_vals = []
plt.legend()
for num in range(20):
  x_vals.append(num)
  y_vals.append(2.7911 - 1.1165*num)

plt.plot(x_vals, y_vals)

plt.title('True Logistic Regressors')
plt.savefig('analysis/logistic_issues_solved.png')
