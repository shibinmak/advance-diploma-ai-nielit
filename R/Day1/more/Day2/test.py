import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

train=pd.read_csv('train.csv', delimiter='\t')
test =pd.read_csv('test.csv',delimiter='\t')
train1=train.as_matrix()
test1=test.as_matrix()

print(train1)
print(test1)

X_train=train1[:,[0,1]]
y_train=train1[:,2]
X_test=test1[:,[0,1]]
y_test=test1[:,2]


knn=KNeighborsClassifier(n_neighbors=3,weights='distance')
knn.fit(X_train,y_train)

print(knn.predict(X_test))

