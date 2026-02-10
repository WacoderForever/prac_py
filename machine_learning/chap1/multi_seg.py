import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

customers = pd.read_csv("data/customers.csv")
sns.set()
df = customers.copy()
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])

points = df.iloc[:, 1:5].values

kmeans = KMeans(n_clusters=6,random_state=0)
kmeans.fit(points)
df['Cluster'] = kmeans.predict(points)

results = pd.DataFrame(columns=['Cluster', 'Average Age', 'Average Income(k$)',
                                'Average Spending Index(0-100)', 'Number of Females',
                                'Number of Males'])

for i,center in enumerate(kmeans.cluster_centers_):
    age = center[1]         #Average age for current cluster
    income = center[2]      #Average income for current cluster 
    spend = center[3]       #Average spending score for current cluster

    gdf = df[df['Cluster']==i]
    females = gdf[gdf['Gender']==0].shape[0]
    males = gdf[gdf['Gender']==1].shape[0]

    results.loc[i] = ([i,age,income,spend,females,males])

print(results)