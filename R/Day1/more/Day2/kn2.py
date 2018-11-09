from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score

import pandas as pd
import numpy as np

train1=pd.read_csv('train.csv', delimiter='\t')
test1=pd.read_csv('test.csv', delimiter='\t')

train=train1.as_matrix()
test=test1.as_matrix()

X_train,X_test=train[:,[0,1]],test[:,[0,1]]
y_train,y_test=train[:,2],test[:,2]

print(X_train.shape)
print(y_train.shape)

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
predictions=knn.predict(X_test)
print(y_test)

print(confusion_matrix(y_test,predictions))
print(accuracy_score(y_test,predictions))
