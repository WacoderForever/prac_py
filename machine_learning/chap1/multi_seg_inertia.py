import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from multi_seg import points

sns.set()

inertias = []

for i in range (1,10):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(points)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,10),inertias)
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()