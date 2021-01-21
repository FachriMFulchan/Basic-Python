import numpy as np

#Soal 1
print ('Soal 1')
A = np.array(([1,2],
             [5,6]))
print ('Matriks A :')
print (A)


B = np.array(([3,5],
             [6,7]))
print ('Matriks B : ')
print (B)

#jika C = 3a + B
#maka det C????

C = (3*A + B)
print('Matriks C :')
print(C)

ans = np.linalg.det(C)
print ('Determinan C : ', int(ans))
print ('\n')
print ('\n')

