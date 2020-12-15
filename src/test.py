import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame

df = DataFrame.from_array(
    [[0, 0, 0.1],
     [1, 0, 0.2],
     [0, 2, 0.5],
     [4,5,0.6]],
    columns = ['scoops of chocolate', 'scoops of vanilla', 'taste rating']
)

print(df.select_columns('scoops of chocolate'))