#beda format baris dan kolom matriks
import numpy as np

a = np.array(((1,2,3),(2,-1,1)))
print ('Matriks A :')
print (a)
b = np.array(((1,2),(2,2),(1,-1)))
print ('Matriks B :')
print (b)

c = np.dot(a,b)
print ('Matriks C:')
print (c)