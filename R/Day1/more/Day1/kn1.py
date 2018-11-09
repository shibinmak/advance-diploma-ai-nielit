from sklearn.datasets import load_iris
iris =load_iris()


print(iris.feature_names)
print(iris.data)
print(iris.target)

X=iris.data
y=iris.target


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)

print(knn)
knn.fit(X,y)

print(knn.predict([[3,5,4,2]]))

from sklearn.metrics import accuracy_score,confusion_matrix

