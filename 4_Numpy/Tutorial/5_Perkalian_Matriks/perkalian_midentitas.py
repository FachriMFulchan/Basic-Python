import numpy as np

a = np.array([(1,2),
              (3,4)])

print ('matriks a :')
print (a)

b = np.identity(2)
print ('matriks b :')
print (b)



c = np.dot(a,b)
print (c)