from scipy.spatial import ConvexHull
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from hull import *


data = datasets.load_wine()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('petal width vs petal length')
plt.xlabel(data.feature_names[2])
plt.ylabel(data.feature_names[3])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    #hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    hullSolution = myConvexHull(bucket)
    print(i)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    # for simplex in hull.simplices:
    #     plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])

    for j in range(len(hullSolution)-1):
        plt.plot((hullSolution[j][0], hullSolution[j+1][0]), (hullSolution[j][1], hullSolution[j+1][1]), colors[i])
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])

plt.show()