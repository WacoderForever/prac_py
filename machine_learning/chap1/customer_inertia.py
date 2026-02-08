import pandas as pd
customers = pd.read_csv("data/customers.csv")

import seaborn as sns
sns.set()

points = customers.iloc[:,3:5].values
inertias = []

from sklearn.cluster import KMeans
for i in range(1,30):
    kmeans = KMeans(n_clusters=i,random_state=0)
    kmeans.fit(points)
    inertias.append(kmeans.inertia_)

import matplotlib.pyplot as plt
plt.plot(range(1,30),inertias)
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()