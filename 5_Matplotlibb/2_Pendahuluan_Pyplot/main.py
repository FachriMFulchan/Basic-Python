import numpy as np
import matplotlib.pyplot as plt

''' ADA 3 STEP UNTUK MEMBUAT GRAFIS
1. Membuat data
2. Membuat plot
3. Menampilkan plot
'''

#1. membuat data
x = np.array((1,2,3,4,5))
y = x ** 2
y2 = y ** 2

#2. membuat plot
plt.plot(x,y)
plt.plot(x,y2)

#3. menampilkan plot
plt.show()