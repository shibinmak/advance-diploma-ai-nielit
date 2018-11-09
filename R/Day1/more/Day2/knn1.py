from sklearn.datasets import load_iris
iris = load_iris()
type(iris)
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
print(knn)

knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))



