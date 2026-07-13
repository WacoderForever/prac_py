import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt

mlp.rcParams['font.family'] = 'serif'

Strike_price = 8000

# Graphical output
Index_levels = np.linspace(7000,9000,100)
Intrinsic_values = np.maximum(Index_levels - Strike_price,0)

plt.figure()
plt.plot(Index_levels,Intrinsic_values,lw=2)
plt.xlabel("Index values")
plt.ylabel("Inner values")
plt.grid(True)
plt.show()