import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from cvxhull import *

iris = datasets.load_iris()
bc = datasets.load_breast_cancer()
wine = datasets.load_wine()
# Load datasets

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['Target'] = pd.DataFrame(iris.target)

bc_df = pd.DataFrame(bc.data, columns=bc.feature_names)
bc_df['Target'] = pd.DataFrame(bc.target)

wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df['Target'] = pd.DataFrame(wine.target)
# Creating dataframe

plt.figure(figsize = (10, 6))
plt.title('Sepal Width VS Sepal Length')
colors = ['b','r','g']
# Configure the visualisation of convex hull

plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
for i in range(len(iris.target_names)):
    bucket = iris_df[iris_df['Target'] == i]
    bucket = bucket.iloc[:,[2,3]].values
    cvxHull = myConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=iris.target_names[i])
    for j in range(len(cvxHull)-1):
        plt.plot((cvxHull[j][0], cvxHull[j+1][0]), (cvxHull[j][1], cvxHull[j+1][1]), colors[i])
plt.legend()
plt.show()
# Replace the feature names and bucket value's index to desired attribute
