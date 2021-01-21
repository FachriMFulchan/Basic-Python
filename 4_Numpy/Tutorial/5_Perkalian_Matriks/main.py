#perkalian matriks
import numpy as np

a = np.array([(1,2),
              (3,4)])
print ('matriks a :')
print (a)


b = np.ones([2,2])
print ('matriks b :')
print (b)



c1 = np.dot(a,b) #cara1
print ('matriks c1 (axb) :')
print (c1)


c2 = a.dot(b) #cara2, kaya OOP
print ('matriks c2 (axb) :')
print (c2)

c3 = np.matmul(a,b) #cara3, pake perintah matmul
print (c3)

'''numpy di linear algebra bisa ngaps aja si
- Determinan
- Trace
- Singular Vektor Decompisition
- Eigenvalues
- Matriks Norm
- Inverse
- Etc.
'''