import numpy as np

a = np.ones((5,5))
print (a)

b = np.zeros((3,3))
print (b)

a[1:4,1:4]=b
print (a)

a[2,2] = 9
print ('hasil akhir : ')
print(a)