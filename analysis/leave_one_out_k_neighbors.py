import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

df = pd.DataFrame(
[['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
['Sugar'       ,     0.02     ,       0.08     ,      0.45     ,     0.45      ],
['Sugar'       ,     0.10     ,       0.15     ,      0.35     ,     0.40      ],
['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ],
['Shortbread'  ,     0.05     ,       0.12     ,      0.28     ,     0.55      ],
['Shortbread'  ,     0.14     ,       0.27     ,      0.31     ,     0.28      ],
['Shortbread'  ,     0.15     ,       0.23     ,      0.30     ,     0.32      ],
['Shortbread'  ,     0.20     ,       0.10     ,      0.30     ,     0.40      ]],
  columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )


arr_reset = df.to_numpy()
accuracies = []
k_list = []
for k in range(1, 19):
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
  accuracies.append(accuracy/19)
  k_list.append(k)


plt.style.use('bmh')
plt.plot(k_list, accuracies)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.xticks(k_list)
plt.title('Leave One Out Cross Validation')
plt.savefig('analysis/leave_one_out.png')
