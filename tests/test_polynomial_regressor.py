import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from dataframe import DataFrame


df = DataFrame.from_array(
    [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)],
    columns = ['x', 'y']
)

print('testing polynomial regressors...')
constant_regressor = PolynomialRegressor(degree=0)
constant_regressor.fit(df, dependent_variable='y')
assert constant_regressor.coefficients == {'constant': 11.333333333333332}
assert round(constant_regressor.predict({'x': 2}), 4) == 11.3333

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(df, dependent_variable='y')
assert linear_regressor.coefficients == {'constant': -3.2380952380952395, 'x': 5.828571428571429}
assert round(linear_regressor.predict({'x': 2}), 4) == 8.4190

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, dependent_variable='y')
assert quadratic_regressor.coefficients == {'constant': 1.1071428571428732, 'x': -0.6892857142857043, 'x^2': 1.3035714285714315}
assert round(quadratic_regressor.predict({'x': 2}), 4) == 4.9429

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, dependent_variable='y')
assert cubic_regressor.coefficients == {'constant': 1.1349206349208627, 'x': -0.8161375661381118, 'x^2': 1.3730158730161168, 'x^3': -0.009259259259297048},cubic_regressor.coefficients
assert round(cubic_regressor.predict({'x': 2}), 4) == 4.9206

quintic_regressor = PolynomialRegressor(degree=5)
quintic_regressor.fit(df, dependent_variable='y')
assert quintic_regressor.coefficients == {'constant': 0.9999999999972258, 'x': -2.949999999727126, 'x^2': 6.958333332801374, 'x^3': -3.9583333331124315, 'x^4': 1.0416666665923966, 'x^5': -0.0916666666615868}, quintic_regressor.coefficients
assert round(quintic_regressor.predict({'x': 2}), 4) == 5.0000
print('passed')
