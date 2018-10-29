
import matplotlib.pyplot as plt;
from sklearn.cluster import KMeans;
import numpy as np;

height = [185.0,170.0,168.0,179.0,182.0,188.0,180.0,180.0,183.0,180.0,180.0,177.0];

weight =[72.0,56.0,60.0,68.0,72.0,77.0,71.0,70.0,84.0,88.0,67.0,76.0];



kmeans = KMeans(n_clusters=3);
X = np.array(list(zip(height,weight)));
kmeans.fit(X);
print("Cluster Centriods");
print("-------------------------------");
print(kmeans.cluster_centers_);
print("-------------------------------");
print("Cluster Labels");
print("-------------------------------");
print(kmeans.labels_);

plt.scatter(height,weight,cmap='rainbow',c=kmeans.labels_);
plt.show();


