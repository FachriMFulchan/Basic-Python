#transpose
#shape
#vektor baris
#reshape

import numpy as np

a = np.array((
              [1,2,3],
              [4,5,6]
              ))

#ukuran matriks (SHAPE)
print ('matriks a dengan ukuran : ', a.shape)
print (a)



#transpose matriks
print ('transpose matriks dari a : ')
print (a.transpose()) #cara1
print (np.transpose(a)) #cara2
print (a.T)



#flatten array, vector baris
print ('flatten matriks a : ')
print (a.ravel())
print (np.ravel(a))




#reshape matriks
print ('reshape matriks a : ')
print (a.reshape(3,2))
print (a.reshape(1,6))
print (a.reshape(6,1))
#yang penting JUMLAH KOMPONEN nya SAMA




#resize matriks, sama kaya reshape cuma PERMANEN
print ('resize matriks a : ')
a.resize(3,2)
print (a)
print ('matriks a dengan ukuran : ', a.shape)