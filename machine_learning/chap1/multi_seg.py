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
print(df.head())