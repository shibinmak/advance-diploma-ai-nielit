from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
iris=load_iris()
print(iris.feature_names)
X=iris.data
y=iris.target
print(X)
print(y)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(y_train.shape)

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
predictions=knn.predict(X_test)
print(y_test)

print(confusion_matrix(y_test,predictions))
print(accuracy_score(y_test,predictions))
