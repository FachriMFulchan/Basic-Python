import numpy as np

a = np.array([[1,2],[2,3]])
b = np.array([[-3,2],[2,-1]])
c = np.array([[1,0],[2,-1]])
print ('Matriks a:')
print (a)
print ('Matriks b:')
print (b)
print ('Matriks c:')
print (c)

a10 = a
for i in range(9):
    f = np.dot(a10,a)
    a10 = f

b11 = b
for i in range(10):
    f = np.dot(b11,b)
    b11 = f

c12 = c
for i in range(11):
    f = np.dot(c12,c)
    c12 = f

x = np.dot(a10,b11)
hasil = np.dot(x,c12)

print('Matriks hasil dari A10*B11*C12 : ')
print (hasil)
print ('Sehingga jumlah unsurnya :',np.sum(hasil))