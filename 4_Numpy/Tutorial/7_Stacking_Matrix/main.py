''' terus kalo array pingin kaya list gimana caranya
DIGABUNGIN GITU GA DITAMBAH
ada method nya namanya STACK (HSTACK, VSTACK)
'''

import numpy as np

#ini array
a = np.array ([1,2,3])
b = np.array ([4,5,6])

c = np.hstack((a,b))
print (c)
d = np.vstack((a,b))
print (d)



#matriks gimana??
aMat = np.zeros((2,3))
bMat = np.ones((2,3))

cMat = np.hstack((aMat,bMat))
print (cMat)
dMat = np.vstack((aMat, bMat))
print (dMat)