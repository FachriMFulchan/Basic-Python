import numpy as np

A = np.array([[1,1,0],[0,1,0],[0,0,1]])
print ('Matriks A :')
print (A)

B=A
for i in range(2009):
    E = np.dot(B,A)
    B = E
print ('Matriks A pangkat 2010:')
print (B)
print ('jumlah unsurnya : ', np.sum(B))