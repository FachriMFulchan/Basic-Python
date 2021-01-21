import numpy as np

a = np.array([
            (1,2,3),
            (4,5,6)
            ])

#shape
print ('matriks a ini berukuran :',a.shape)
print (a)


#transpose
print ('transpose matriks')
print (np.transpose(a))


#flatten
print ('flatten matriks')
print (np.ravel(a))

#reshape
print ('reshape matriks')
print (np.reshape(a, (3,2)))

#resize
print ('resize matriks')
print (np.resize(a, (3,2)))
