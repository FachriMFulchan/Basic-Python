import numpy as np

#A . X = C, Tentukan matriks X
print ('Matriks A : ')
A = np.array(([1,-4],[0,2]))
print (A)

print ('Matriks B : ')
C = np.array(([-10,5],[6,-2]))
print (C)

#X = Ainv * C
A_inv = np.linalg.inv(A)
X = np.dot(A_inv , C)
print ('Matriks X : ')
print (X)