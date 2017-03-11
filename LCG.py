from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import os

def lcg (X, a, c, m):
    return (a * X + c) % m;

X = []
Y = []
Z = []

n = int(input("N : "))

prev = 0
for i in range(n):
    prev = lcg(prev,43,5,4096)
    if i % 3 == 0:
        X.append(prev)
    elif i % 3 == 1:
        Y.append(prev)
    else:
        Z.append(prev)

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')
ax.set_title('N = ' + str(n))

scat = ax.scatter(X, Y, Z)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0

mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

i = 0
while os.path.exists('fig%s.png' % i):
    i += 1

plt.savefig('fig' + str(i) + '.png')
plt.show()