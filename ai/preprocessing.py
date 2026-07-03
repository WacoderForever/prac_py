import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]])

# Binarization data
data_binarized = preprocessing.Binarizer(threshold = 2.1).transform(input_data)
print(f"Binarized data:\n{data_binarized}")

# Mean removal
print(f"\nBefore:\n Mean: {input_data.mean(axis=0)}\n Std Dev: {input_data.std(axis=0)}\n")
data_scaled = preprocessing.scale(input_data)
print(f"Data scaled: {data_scaled}\n")
print(f"\nAfter:\n Mean: {data_scaled.mean(axis=0)}\n Std Dev: {data_scaled.std(axis=0)}\n")

# MinMax Scaling
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)

# Normalize data
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1') # Least absolute deviations(more robust)
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2') # Least Squares
print("\nL1 normalized data:\n", data_normalized_l1)
print("\nL2 normalized data:\n", data_normalized_l2)