#KNN on different data
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

train = pd.read_csv('./KNN4-train.csv', delimiter='\t')   # better be in the correct directory!
test = pd.read_csv('./KNN4-test.csv',  delimiter='\t')

print(train.head())
print(test.head())

print(type(train))
print(type(test))

trainArr1 = train.as_matrix()
testArr1 = test.as_matrix()
trainArr=trainArr1[:,[0,1]]
trainRes = trainArr1[:,[2]]
testArr = testArr1[:,[0,1]]
testRes = testArr1[:,[2]]


print(testArr)
print(testRes)
print(trainArr)
print(trainRes)

print(type(train))
print(type(test))

knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
knn.fit(trainArr, trainRes)
output = knn.predict(testArr)

print(output)
print(testRes)





