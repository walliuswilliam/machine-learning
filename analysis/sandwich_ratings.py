import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

# df = DataFrame.from_array(
#     [[0,0,1],    
#      [1,0,2],
#      [2,0,4],
#      [4,0,8],
#      [6,0,9],
#      [0,2,2],
#      [0,4,5],
#      [0,6,7],
#      [0,8,6]
#     ],
#     columns = ['Slices of Roast Beef', 'Tablespoons of Peanut Butter', 'Rating']
# )

# regressor = LinearRegressor(df, dependent_variable='Rating')

# print(regressor.coefficients)


# df = DataFrame.from_array(
#     [[0, 0, 1], 
#     [1, 0, 2], 
#     [2, 0, 4], 
#     [4, 0, 8], 
#     [6, 0, 9], 
#     [0, 2, 2], 
#     [0, 4, 5], 
#     [0, 6, 7], 
#     [0, 8, 6],
#     [2, 2, 0],
#     [3, 4, 0]],
#     columns = ['beef', 'pb', 'rating']
# )

# df = df.create_interaction_terms('beef', 'pb')

# assert df.columns == ['beef', 'pb', 'rating', 'beef * pb']
# print('passed columns')
# assert df.to_array() == [[0, 0, 1, 0], 
#     [1, 0, 2, 0], 
#     [2, 0, 4, 0], 
#     [4, 0, 8, 0], 
#     [6, 0, 9, 0], 
#     [0, 2, 2, 0], 
#     [0, 4, 5, 0], 
#     [0, 6, 7, 0], 
#     [0, 8, 6, 0],
#     [2, 2, 0, 4],
#     [3, 4, 0, 12]], df.to_array
# print('passed to_array')

# regressor = LinearRegressor(df, dependent_variable='rating')

# print(regressor.coefficients)

# print(regressor.predict({'beef': 5, 'pb': 0, 'beef * pb': 0}))

# print(regressor.predict({'beef': 5, 'pb': 5, 'beef * pb': 25}))


# df = DataFrame.from_array(
#     [[0, 0, 1], 
#     [1, 0, 2], 
#     [2, 0, 4], 
#     [4, 0, 8], 
#     [6, 0, 9], 
#     [0, 2, 2], 
#     [0, 4, 5], 
#     [0, 6, 7], 
#     [0, 8, 6],
#     [2, 2, 0.1],
#     [3, 4, 0.1]],
#     columns = ['beef', 'pb', 'rating']
# )

# df = df.create_interaction_terms('beef', 'pb')

# regressor = LogisticRegressor(df, dependent_variable='rating', upper_bound=10)

# print(regressor.coefficients)

# print(regressor.predict({'beef': 5, 'pb': 0, 'beef * pb': 0}))

# print(regressor.predict({'beef': 12, 'pb': 0, 'beef * pb': 0}))

# print(regressor.predict({'beef': 5, 'pb': 5, 'beef * pb': 25}))


#Linear Regressor
print('Linear Regressor')

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating'])

df = df.create_dummy_variables('condiments')

df = df.create_interaction_terms('beef', 'pb')
df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo',)
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')

regressor = LinearRegressor(df, dependent_variable='rating')

print('Coefficients', regressor.coefficients)


print('8 beef, mayo', regressor.predict({'beef': 8, 'pb': 0, 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 0}))

print('4 pb, jelly', regressor.predict({'beef': 0, 'pb': 4, 'mayo': 0, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 4, 'mayo * jelly': 0}))

print('4 pb, mayo', regressor.predict({'beef': 0, 'pb': 4, 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))

print('4 pb, 8 beef, mayo', regressor.predict({'beef': 8, 'pb': 4, 'mayo': 1, 'jelly': 0, 'beef * pb': 32, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))

print('8 beef, mayo, jelly', regressor.predict({'beef': 8, 'pb': 0, 'mayo': 1, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 8, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 1}))



#Logistic Regressor
print('\nLogistic Regressor')

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0.1],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0.1],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0.1],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0.1],
    [5, 5, [],                0.1],
    [5, 5, ['mayo'],          0.1],
    [5, 5, ['jelly'],         0.1],
    [5, 5, ['mayo', 'jelly'], 0.1]],
    columns = ['beef', 'pb', 'condiments', 'rating'])

df = df.create_dummy_variables('condiments')

df = df.create_interaction_terms('beef', 'pb')
df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo',)
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')

regressor = LogisticRegressor(df, dependent_variable='rating', upper_bound=10)

print('Coefficients', regressor.coefficients)


print('8 beef, mayo', regressor.predict({'beef': 8, 'pb': 0, 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 0}))

print('4 pb, jelly', regressor.predict({'beef': 0, 'pb': 4, 'mayo': 0, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 4, 'mayo * jelly': 0}))

print('4 pb, mayo', regressor.predict({'beef': 0, 'pb': 4, 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))

print('4 pb, 8 beef, mayo', regressor.predict({'beef': 8, 'pb': 4, 'mayo': 1, 'jelly': 0, 'beef * pb': 32, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))

print('8 beef, mayo, jelly', regressor.predict({'beef': 8, 'pb': 0, 'mayo': 1, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 8, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 1}))