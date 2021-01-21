import numpy as np

print ('Matriks A : ')
A = np.array(([1,3],
              [-2,1]))
print(A)
print ('Matriks B : ')
B = np.array(([1,5],
              [-7,-2]))
print (B)

C = (3*A) - (2*B)
print ('Matriks C : ')
print (C)

C_inv = np.linalg.inv(C)
print ('Matriks Invers C : ')
print (C_inv)


