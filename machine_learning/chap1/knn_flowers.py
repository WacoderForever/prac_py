import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['class'] = iris.target
df['class name'] = iris.target_names[iris.target]

# splitting training and test data
x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=0)

# training the model
model = KNeighborsClassifier(n_neighbors=10)
model.fit(x_train,y_train)

print(model.score(x_test,y_test))
print(model.predict([[5.6, 4.4, 1.2, 0.4]]))