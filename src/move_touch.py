#prints upsude down astablet was upsuide down
import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fname = sys.argv[1]
size = sys.argv[2]
#data = []
ln = -1
#set up the x and y coordinate matrices
xs = np.zeros((int(size), 10))
ys = np.zeros((int(size), 10))

with open(fname, 'rb') as f:
    datum = f.readlines()
    for d in datum:
        ln += 1
        spl_d = d.split('&')
        x = 0.0
        y = 0.0
        point = None
        #d = ['0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0', '0.0','0.0']
        for s in spl_d:
            spl_s = s.split('=')
            if spl_s[0] == "x":
                x = spl_s[1]
            if spl_s[0] == "y":
                y = spl_s[1]
            if spl_s[0] == "pointer":
                xs[ln][int(spl_s[1])] = str(x)
                ys[ln][int(spl_s[1])] = str(y)

fig = plt.figure(figsize=(20,15))
#ax = fig.add_subplot(1,1,1)
#ax = fig.gca(projection='3d')
plt.scatter(xs,ys,c=('b','g','r','c','m','y','k','w'))
#ax.scatter(xs,ys, c=('b','g','r','c','m','y','k','w'))
plt.title('Movement data from an Android with swirl paper')

#set ranges and limits
#ax.set_zlim(0, 1)
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')

#ax.view_init(elev=20., azim=-35)
#plt.show()
fig.savefig(fname + "movement.png")
        #if pressure != 0:
           
            #for i in xrange(9):
            #    with open(str(i) + ".txt", 'a') as f:
            #       f.write(str(d[i]) + "\n")

