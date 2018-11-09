from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris()
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target

print(type(X))
knn=KNeighborsClassifier(n_neighbors=1)
print(knn)
knn.fit(X,y)

print(knn.predict([[3,5,4,2],[3,4,5,6]]))

#print(knn.predict(X[[1],:])


