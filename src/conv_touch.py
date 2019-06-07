import sys
import numpy as np
import matplotlib.pyplot as plt

fname = sys.argv[1]
size = sys.argv[2]
#data = []
ln = -1
data = np.zeros((int(size), 10))
with open(fname, 'rb') as f:
    datum = f.readlines()
    for d in datum:
        ln += 1
        spl_d = d.split('&')
        pressure = 0.0
        point = None
        #d = ['0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0', '0.0','0.0']
        for s in spl_d:
            spl_s = s.split('=')
            if spl_s[0] == "pressure":
                pressure = spl_s[1]
            if spl_s[0] == "pointer":
                data[ln][int(spl_s[1])] = str(pressure)

fig = plt.figure(figsize=(40,20))
plt.plot(data)
plt.title('Pressure data from an Android with swirl paper')
plt.ylabel('Pressure')
#plt.show()
fig.savefig(fname+"pressure.png")
        #if pressure != 0:
           
            #for i in xrange(9):
            #    with open(str(i) + ".txt", 'a') as f:
            #       f.write(str(d[i]) + "\n")

