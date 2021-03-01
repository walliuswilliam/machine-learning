import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from dataframe import DataFrame
import matplotlib.pyplot as plt

dataset = [
  (-4, 11.0),
  (-2, 5.0),
  (0, 3.0),
  (2, 5.0),
  (4, 11.1),
  (6, 21.1),
  (8, 35.1),
  (10, 52.8),
  (12, 74.8),
  (14, 101.2)]

training = [dataset[point_index] for point_index in range(len(dataset)) if not point_index % 2]
testing = [dataset[point_index] for point_index in range(len(dataset)) if point_index % 2]


df = DataFrame.from_array(training, columns = ['x', 'y'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(df, 'y')

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, 'y')

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, 'y')

quartic_regressor = PolynomialRegressor(degree=4)
quartic_regressor.fit(df, 'y')


def rss_calc(input_list, regressor):
  rss_sum = 0
  for (a,b) in input_list:
    rss_sum += (b-regressor.predict({'x': a}))**2
  return rss_sum

print('training')
print('linear_regressor', rss_calc(training, linear_regressor))
print('quadratic_regressor', rss_calc(training, quadratic_regressor))
print('cubic_regressor', rss_calc(training, cubic_regressor))
print('quartic_regressor', rss_calc(training, quartic_regressor), '\n')


print('testing')
print('linear_regressor', rss_calc(testing, linear_regressor))
print('quadratic_regressor', rss_calc(testing, quadratic_regressor))
print('cubic_regressor', rss_calc(testing, cubic_regressor))
print('quartic_regressor', rss_calc(testing, quartic_regressor))


plt.style.use('bmh')

regressors = [linear_regressor, quadratic_regressor, cubic_regressor, quartic_regressor]
for regressor in regressors:
  x_vals = []
  y_vals = []
  for x in range(-5, 21):
    x_vals.append(x)
    y_vals.append(regressor.predict({'x': x}))
  plt.plot(x_vals, y_vals)

train = [[point[0] for point in training], [point[1] for point in training]]
test = [[point[0] for point in testing], [point[1] for point in testing]]
plt.plot(train[0], train[1], 'ro')
plt.plot(test[0], test[1], 'bo')

regressor_names = ['linear_regressor', 'quadratic_regressor', 'cubic_regressor', 'quartic_regressor']
legend = [regressor for regressor in regressor_names]
legend.append('Training')
legend.append('Testing')
plt.legend(legend)
plt.title('Training/Testing Sets')
plt.savefig('analysis/training_testing.png')
