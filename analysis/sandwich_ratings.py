import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from dataframe import DataFrame

df = DataFrame.from_array(
    [[0,0,1],    
     [1,0,2],
     [2,0,4],
     [4,0,8],
     [6,0,9],
     [0,2,2],
     [0,4,5],
     [0,6,7],
     [0,8,6]
    ],
    columns = ['Slices of Roast Beef', 'Tablespoons of Peanut Butter', 'Rating']
)

regressor = LinearRegressor(df, dependent_variable='Rating')

print(regressor.coefficients)