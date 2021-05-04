import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


unnormalized = pd.read_csv('datasets/book_type.csv')

def classify_book(x):
  if 'adult' in x:
    return 1
  else:
    return 0

unnormalized['book type'] = unnormalized['book type'].apply(classify_book)
unnormalized = unnormalized[['book type','num pages','num unique words','avg sentence length','avg word size']]


simple_scaling = unnormalized.copy()
min_max = unnormalized.copy()
z_score = unnormalized.copy()


for column in simple_scaling:
  if column != 'book type':
    simple_scaling[column] = simple_scaling[column]/max(unnormalized[column])

for column in min_max:
  if column != 'book type':
    min_max[column] = (min_max[column]-min(unnormalized[column]))/(max(unnormalized[column])-min(unnormalized[column]))

for column in z_score:
  if column != 'book type':
    z_score[column] = z_score[column].apply(lambda x: ((x - unnormalized[column].mean())/unnormalized[column].std()))

df_list = [unnormalized, simple_scaling, min_max, z_score]

plt.style.use('bmh')
k_list = [x for x in range(100) if x%2 == 1]
for df in df_list:
  arr_reset = df.to_numpy()
  accuracies = []
  
  for k in k_list:
    accuracy = 0
    for row_index in range(len(arr_reset)):
      arr = arr_reset.copy()
      real_value = arr[row_index][0]
      observation = arr[row_index][1:]
      arr = np.delete(arr, row_index, 0)

      y = [row[0] for row in arr]
      x = np.delete(arr, 0, 1)

      knn = KNeighborsClassifier(n_neighbors=k)
      knn.fit(x, y)
      prediction = knn.predict([observation])[0]
      if prediction == real_value:
        accuracy += 1
    accuracies.append(accuracy/df.shape[0])
  plt.plot(k_list, accuracies)


plt.xlabel('k')
plt.ylabel('accuracy')
plt.legend(['unnormalized', 'simple_scaling', 'min_max', 'z_score'])
plt.title('Leave-One-Out Accuracy for Various Normalizations')
plt.savefig('analysis/normalized_knn.png')