import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

# df = DataFrame.from_array(
#     [[1,0.2],
#      [2,0.25],
#      [3,0.5]],
#     columns = ['x','y']
# )

# log_reg = LogisticRegressor(df, dependent_variable = 'y', upper_bound = 1)

# print('printing coefficients...')
# print(log_reg.coefficients)
# print('passed')

# print('\ntesting predict...')
# assert round(log_reg.predict({'x': 5}), 3) == 0.777, log_reg.predict({'x': 5})
# print('passed')


# df = DataFrame.from_array(
#     [[0, 0, [],               1],
#     [0, 0, ['mayo'],          1],
#     [0, 0, ['jelly'],         4],
#     [0, 0, ['mayo', 'jelly'], 0.1],
#     [5, 0, [],                4],
#     [5, 0, ['mayo'],          8],
#     [5, 0, ['jelly'],         1],
#     [5, 0, ['mayo', 'jelly'], 0.1],
#     [0, 5, [],                5],
#     [0, 5, ['mayo'],          0.1],
#     [0, 5, ['jelly'],         9],
#     [0, 5, ['mayo', 'jelly'], 0.1],
#     [5, 5, [],                0.1],
#     [5, 5, ['mayo'],          0.1],
#     [5, 5, ['jelly'],         0.1],
#     [5, 5, ['mayo', 'jelly'], 0.1]],
#     columns = ['beef', 'pb', 'condiments', 'rating'])

# df = df.create_dummy_variables('condiments')

# df = df.create_interaction_terms('beef', 'pb')
# df = df.create_interaction_terms('beef', 'mayo')
# df = df.create_interaction_terms('beef', 'jelly')
# df = df.create_interaction_terms('pb', 'mayo',)
# df = df.create_interaction_terms('pb', 'jelly')
# df = df.create_interaction_terms('mayo', 'jelly')

# logistic_regressor = LogisticRegressor(df, dependent_variable='rating', upper_bound=10)


# print('testing observation 1...')
# observation = {'beef': 8, 'mayo': 1}
# assert round(logistic_regressor.predict(observation), 2) == 9.72
# print('passed')

# print('testing observation 2...')
# # test 4 tbsp of pb + 8 slices of beef + mayo
# observation = {'beef': 8, 'pb': 4, 'mayo': 1}
# assert round(logistic_regressor.predict(observation), 2) == 0.77
# print('passed')

# print('testing observation 3...')
# # test 8 slices of beef + mayo + jelly
# observation = {'beef': 8, 'mayo': 1, 'jelly': 1}
# assert round(logistic_regressor.predict(observation), 2) == 0.79
# print('passed')


print('testing logistic gradient descent')
df = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    columns = ['x', 'y'])

reg = LogisticRegressor(df, dependent_variable='y', upper_bound=1)

reg.set_coefficients({'constant': 0.5, 'x': 0.5})

alpha = 0.01
delta = 0.01
num_steps = 20000

reg.gradient_descent(alpha, delta, num_steps, debug_mode=True)

assert {key:round(reg.coefficients[key],4) for key in reg.coefficients} == {'constant': 2.7911, 'x': -1.1165}, {key:round(reg.coefficients[key],4) for key in reg.coefficients}
print('passed')
