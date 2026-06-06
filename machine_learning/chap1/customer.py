import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

sns.set()

customers = pd.read_csv("data/customers.csv")

points = customers.iloc[:, 3:5].values
x = points[:,0]
y = points[:,1]

kmeans = KMeans(n_clusters=5,random_state=0)
kmeans.fit(points)
predicted_cluster_indexes = kmeans.predict(points)
centers = kmeans.cluster_centers_

plt.scatter(x,y,c=predicted_cluster_indexes,cmap='viridis',alpha=0.7,s=50)
plt.scatter(centers[:,0],centers[:,1],c='red',s=100)



plt.xlabel("Annual Income k$")
plt.ylabel("Spending Score")
plt.show()

