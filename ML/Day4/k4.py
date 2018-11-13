from sklearn.datasets.samples_generator import make_moons
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
X,y_true=make_moons(200,noise=0.05)
kmeans=KMeans(2)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],c=y_kmeans)
plt.show()

from sklearn.cluster import SpectralClustering
model=SpectralClustering(2,affinity='nearest_neighbors')

#model=SpectralClustering(2,affinity='nearest_neighbors',assign_labels='kmeans')
labels=model.fit_predict(X)
plt.scatter(X[:,0],X[:,1],c=labels,s=50,cmap='viridis')
plt.show()

