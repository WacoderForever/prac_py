import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

print("Please be patient while I do importing & plotting")

delta = 0.1
x = plt.arange( -3., 3., delta)
y = plt.arange( -3., 3., delta)

X, Y = plt.meshgrid(x,y)
Z = plt.sin(X)*plt.cos(Y)
fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X,Y,Z)
ax.plot_wireframe(X,Y,Z,color='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()