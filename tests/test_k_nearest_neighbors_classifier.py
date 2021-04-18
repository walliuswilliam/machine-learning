import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
import pandas as pd
import numpy as np

df = pd.DataFrame(
    [['Shortbread' ,  0.14  ,    0.14  ,   0.28  ,  0.44],
    ['Shortbread'  ,  0.10  ,    0.18  ,   0.28  ,  0.44],
    ['Shortbread'  ,  0.12  ,    0.10  ,   0.33  ,  0.45],
    ['Shortbread'  ,  0.10  ,    0.25  ,   0.25  ,  0.40],
    ['Sugar'       ,  0.00  ,    0.10  ,   0.40  ,  0.50],
    ['Sugar'       ,  0.00  ,    0.20  ,   0.40  ,  0.40],
    ['Sugar'       ,  0.10  ,    0.08  ,   0.35  ,  0.47],
    ['Sugar'       ,  0.00  ,    0.05  ,   0.30  ,  0.65],
    ['Fortune'     ,  0.20  ,    0.00  ,   0.40  ,  0.40],
    ['Fortune'     ,  0.25  ,    0.10  ,   0.30  ,  0.35],
    ['Fortune'     ,  0.22  ,    0.15  ,   0.50  ,  0.13],
    ['Fortune'     ,  0.15  ,    0.20  ,   0.35  ,  0.30],
    ['Fortune'     ,  0.22  ,    0.00  ,   0.40  ,  0.38]],
    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )

knn = KNearestNeighborsClassifier(k=5)
knn.fit(df, dependent_variable = 'Cookie Type')
observation = {
    'Portion Eggs': 0.10,
    'Portion Butter': 0.15,
    'Portion Sugar': 0.30,
    'Portion Flour': 0.45
  }

print(knn.classify(observation)) #'Shortbread'


df = pd.DataFrame(
    [['A', 0],
  ['A', 1],
  ['B', 2],
  ['B', 3]],
  columns = ['letter', 'number']
)

knn = KNearestNeighborsClassifier(k=4)
knn.fit(df, dependent_variable = 'letter')
observation = {
    'number': 1.6
}

print(knn.classify(observation)) #'B'
