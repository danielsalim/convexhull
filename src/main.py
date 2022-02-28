import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from cvxhull import *

iris = datasets.load_iris()
bc = datasets.load_breast_cancer()
wine = datasets.load_wine()
# Loading datasets

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['Target'] = pd.DataFrame(iris.target)

bc_df = pd.DataFrame(iris.data, columns=iris.feature_names)
bc_df['Target'] = pd.DataFrame(iris.target)

wine_df = pd.DataFrame(iris.data, columns=iris.feature_names)
wine_df['Target'] = pd.DataFrame(iris.target)
# Creating dataframe

# Configure the visualisation of convex hull
import matplotlib.pyplot as plt
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width VS Petal Length')

# Select which atribute to be test
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
for i in range(len(iris.target_names)):
    bucket = iris_df[iris_df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = myConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=iris.target_names[i])
    for j in range(len(hull)-1):
        plt.plot((hull[j][0], hull[j+1][0]), (hull[j][1], hull[j+1][1]), colors[i])
plt.legend()
plt.show()