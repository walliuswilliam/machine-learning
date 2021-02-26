import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from dataframe import DataFrame
import matplotlib.pyplot as plt


df = DataFrame.from_array([
  (1, 3.1),
  (2, 10.17),
  (3, 20.93),
  (4, 38.71),
  (5, 60.91),
  (6, 98.87),
  (7, 113.92),
  (8, 146.95),
  (9, 190.09),
  (10, 232.65)],
  columns = ['Time', 'Distance'])

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, 'Distance')

print('quadratic_regressor')
print('Time = 5:', quadratic_regressor.predict({'Time': 5}))
print('Time = 10:', quadratic_regressor.predict({'Time': 10}))
print('Time = 200:', quadratic_regressor.predict({'Time': 200}))


cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, 'Distance')

print('\ncubic_regressor')
print('Time = 5:', cubic_regressor.predict({'Time': 5}))
print('Time = 10:', cubic_regressor.predict({'Time': 10}))
print('Time = 200:', cubic_regressor.predict({'Time': 200}))


plt.style.use('bmh')
quadratic_x = []
quadratic_y = []
for second in range(201):
  quadratic_x.append(second)
  quadratic_y.append(quadratic_regressor.predict({'Time': second}))
plt.plot(quadratic_x, quadratic_y)

plt.style.use('bmh')
cubic_x = []
cubic_y = []
for second in range(201):
  cubic_x.append(second)
  cubic_y.append(cubic_regressor.predict({'Time': second}))
plt.plot(cubic_x, cubic_y)

plt.legend(['Quadratic','Cubic'])

plt.title('Rocket Takeoff')
plt.savefig('analysis/rocket.png')
