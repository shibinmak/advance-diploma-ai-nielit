from sklearn.datasets import load_iris
iris =load_iris()


print(iris.feature_names)
print(iris.data)
print(iris.target)

X=iris.data
y=iris.target


from sklearn.neighbors import KNeighborsClassifier
knn1=KNeighborsClassifier(n_neighbors=1)

knn5=KNeighborsClassifier(n_neighbors=7)


from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


knn1.fit(X_train,y_train)

knn5.fit(X_train,y_train)


predictions1=knn1.predict(X_test)

predictions5=knn5.predict(X_test)

print(accuracy_score(y_test,predictions1))
print(confusion_matrix(y_test,predictions1))



print(accuracy_score(y_test,predictions5))
print(confusion_matrix(y_test,predictions5))



