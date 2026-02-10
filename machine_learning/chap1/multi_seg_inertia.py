import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder 

customers = pd.read_csv('data/customers.csv')
sns.set()
df = customers.copy()
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])

points = df.iloc[:,1:5].values

inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,random_state=0)
    kmeans.fit(points)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11),inertias)
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()