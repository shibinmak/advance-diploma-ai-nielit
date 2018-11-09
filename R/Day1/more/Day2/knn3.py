#cross validation
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score

iris = load_iris()
type(iris)
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target
knn=KNeighborsClassifier(n_neighbors=3)
print(knn)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn.fit(X_train,y_train)
predictions=knn.predict(X_test)
print (accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))

scores=cross_val_score(knn,X,y,cv=20,scoring='accuracy')
print(scores)


