#knn=5
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
type(iris)
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target
knn=KNeighborsClassifier(n_neighbors=5)
print(knn)
knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))



