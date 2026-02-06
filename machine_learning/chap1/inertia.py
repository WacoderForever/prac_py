import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import seaborn as sns

sns.set()

points, cluster_indexes = make_blobs(n_samples=300, cluster_std=0.8, random_state=0)

inertias = []

for i in range(1,10):
    kmeans = KMeans(n_clusters=i,random_state=0)
    kmeans.fit(points)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,10),inertias)
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()