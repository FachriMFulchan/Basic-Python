import numpy as np

#Soal 2
print ('Soal 2')
print ('Matriks B : ')
B = np.array(([5,1],
              [-1,-2]))
print (B)
print ('Matriks C : ')
C= np.array(([9,9],
             [7,-4]))
print (C)
print ('A.B = C','Tentukan Matriks A..')
print ('A = C.invB')

B_inv = np.linalg.inv(B)
A = np.dot(C,B_inv)
print ('Matriks A : ')
print (A)
