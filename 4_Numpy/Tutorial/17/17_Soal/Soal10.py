import numpy as np

A = np.array([[2,1],[0,4]])
print (A)
B = np.array([[-3],[-6]])
print (B)

C=A
for i in range(5):
    E = np.dot(C,A)
    C = E

hasil = np.dot(C,B)
print (hasil)
print (hasil/2**12)
