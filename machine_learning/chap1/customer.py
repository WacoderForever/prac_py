import pandas as pd
customers = pd.read_csv("data/customers.csv")

import seaborn as sns
sns.set()
points = customers.iloc[:,3:5].values

x = points[:,0]
y = points[:,1]

import matplotlib.pyplot as plt
plt.xlabel("Annual Income k$")
plt.ylabel("Spending Score")

from sklearn.cluster import KMeans

kmeans=KMeans(n_clusters=5,random_state=0)
kmeans.fit(points)
predicted_cluster_indexes = kmeans.predict(points)

plt.scatter(x,y,c=predicted_cluster_indexes,alpha=0.7,s=50,cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='red',s=100)
plt.show()

df = customers.copy()
df["Cluster"] = kmeans.predict(points)
print(df)

import numpy as np
# Get the cluster index for a customer with a high income and low spending score
cluster = kmeans.predict(np.array([[120, 20]]))[0]
# Filter the DataFrame to include only customers in that cluster
clustered_df = df[df['Cluster'] == cluster]
# Show the customer IDs
print(clustered_df['CustomerID'].values)