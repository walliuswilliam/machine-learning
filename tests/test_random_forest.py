import sys
sys.path.append('src')
sys.path.append('datasets')
from random_forest import *
from semi_random import *
import random


data = create_random_dataset()
forest = RandomForest(data)

print(data[1][0])
print(forest.predict(data[1][0]))

print(data[2][0])
print(forest.predict(data[2][0]))