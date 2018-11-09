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
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


knn.fit(X_train,y_train)
predictions=knn.predict(X_test)

print(accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))
