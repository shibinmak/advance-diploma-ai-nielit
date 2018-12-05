from  sklearn.datasets import load_boston
data=load_boston()
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
mlp=MLPRegressor()
X=data.data
y=data.target
mlp.fit(X,y)

p=mlp.predict(X)
print(mean_squared_error(y,p))


