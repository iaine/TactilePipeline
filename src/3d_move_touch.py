#prints upsude down astablet was upsuide down
#import bpy
#from bpy.props import *
import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fname = sys.argv[1]
size = sys.argv[2]
#position data
data = []
ln = -1
#set up the x and y coordinate matrices
xs = np.zeros((int(size), 10))
ys = np.zeros((int(size), 10))
zs = np.zeros((int(size), 10))
with open(fname, 'r') as f:
    datum = f.readlines()
    for d in datum:
        ln += 1
        spl_d = d.split('&')
        x = 0.0
        y = 0.0
        z = 0.0
        point = None
        #d = ['0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0', '0.0','0.0']
        for s in spl_d:
            spl_s = s.split('=')
            if spl_s[0] == "x":
                x = spl_s[1]
            if spl_s[0] == "y":
                y = spl_s[1]
            if spl_s[0] == "pressure":
                z = spl_s[1]
            if spl_s[0] == "pointer":
                xs[ln][int(spl_s[1])] = str(x)
                ys[ln][int(spl_s[1])] = str(y)
                zs[ln][int(spl_s[1])] = str(z)

fig = plt.figure(figsize=(20,15))
ax = fig.add_subplot(1,1,1, projection='3d')
#ax = fig.gca(projection='3d')
#plt.scatter(xs,ys,c=('b','g','r','c','m','y','k','w'))
ax.scatter(xs,ys, zs, c=('b','g','r','c','m','y','k','w'))

#set ranges and limits
ax.set_zlim(0, 0.25)
ax.set_xlabel('X pixel position')
ax.set_ylabel('Y pixel position')
ax.set_zlabel('Pressure applied')

#ax.view_init(elev=20., azim=-35)
fig.savefig("3d.png")
