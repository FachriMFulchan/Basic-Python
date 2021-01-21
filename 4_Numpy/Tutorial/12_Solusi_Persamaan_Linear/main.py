import numpy as np

A = np.array(((2,3), (1,2)))
W = np.array(23)
X = np.array(14)
Y = np.vstack((W,X))
print (Y)


print ('A invers')
inv_A = np.linalg.inv(A)

#menyelesaikan persamaan linear
print ('A Invers dikali Y')
Z1 = np.dot(inv_A,Y)
print (Z1)


#cara lain
Z2 = np.linalg.solve(A,Y)
print (Z2)