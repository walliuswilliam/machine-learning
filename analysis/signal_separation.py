import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from dataframe import DataFrame
import math
import matplotlib.pyplot as plt

data = [(0.0, 7.0),
 (0.2, 5.6),
 (0.4, 3.56),
 (0.6, 1.23),
 (0.8, -1.03),
 (1.0, -2.89),
 (1.2, -4.06),
 (1.4, -4.39),
 (1.6, -3.88),
 (1.8, -2.64),
 (2.0, -0.92),
 (2.2, 0.95),
 (2.4, 2.63),
 (2.6, 3.79),
 (2.8, 4.22),
 (3.0, 3.8),
 (3.2, 2.56),
 (3.4, 0.68),
 (3.6, -1.58),
 (3.8, -3.84),
 (4.0, -5.76),
 (4.2, -7.01),
 (4.4, -7.38),
 (4.6, -6.76),
 (4.8, -5.22)]

signals = [(math.sin(x), math.cos(x), math.sin(2*x), math.cos(2*x), y) for (x,y) in data]

df = DataFrame.from_array(signals, ['sin(x)', 'cos(x)', 'sin(2x)', 'cos(2x)', 'y'])

regressor = LinearRegressor(df, 'y')
print('\ncoefficients', regressor.coefficients)


plt.style.use('bmh')
x_list = [point[0] for point in data]
y_list = [point[1] for point in data]
plt.plot(x_list,y_list, 'ro')


x_points = []
y_points = []
for x_indx in range(5001):
  x = x_indx/1000
  y = regressor.predict({'sin(x)': math.sin(x), 'cos(x)': math.cos(x), 'sin(2x)': math.sin(2*x), 'cos(2x)': math.cos(2*x)})
  x_points.append(x)
  y_points.append(y)
plt.plot(x_points,y_points)


plt.legend(['Data Points','Curve'])
plt.title('Signal Separation')
plt.savefig('analysis/signal.png')