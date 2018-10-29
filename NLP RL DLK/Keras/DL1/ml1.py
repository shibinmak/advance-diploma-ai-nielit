
from keras.models import Sequential
from keras.layers import Dense
import numpy



seed = 7
numpy.random.seed(seed)



dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")


X = dataset[:,0:8]
Y = dataset[:,8]


model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X, Y, epochs=150, batch_size=10,  verbose=2)


predictions = model.predict(X)


rounded = [round(x[0]) for x in predictions]
print(rounded)