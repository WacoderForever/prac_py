import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

sns.set()

customer = pd.read_csv('data/customers.csv')

df = customer.copy()
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])

points = df.iloc[:,1:5].values

kmeans = KMeans(n_clusters=6,random_state=0)
kmeans.fit(points)

df['Cluster'] = kmeans.predict(points)

results = pd.DataFrame(columns = ['Cluster','Average Age','Average Income',
                                  'Average Spending Index','Number of Females','Number of Males'])

for i,center in enumerate(kmeans.cluster_centers_):
    age = center[1]         # Average age for a cluster
    income = center[2]      # Average income for a cluster
    spending = center[3]    # Average spending index for a cluster

    gdf = df[df['Cluster']==i]
    females = gdf[gdf['Gender'] == 0].shape[0]
    males = gdf[gdf['Gender'] == 1].shape[0]

    results.loc[i] = ([i,age,income,spending,females,males])

print(results)

