import numpy as np


#membuat array
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2, 2.5, 3, 3.5])


#membuat array dengan range ('arange' namanya kalo di numpy)
c = np.arange(1, 10, 4)


#membuat linear space
d = np.linspace(2,10,5)
#nampilin 5 angka dari jarak 1-10, misal
#rumusnya (angkamax-angkamin) / banyak angka yang mau ditampilin-1



#array multidimensi (MATRIKS)
e = np.array ( [ (1,2,3),(4,5,6) ] )



#ARRAY DAN MATRIKS NOL
f = np.zeros(5) #array

g = np.zeros((5,5)) #matriks



#ARRAY DAN MATRIKS SATUAN
h = np.ones (5)
i = np.ones ((5,5))




#MATRIKS IDENTITAS
j1 = np.identity(5)
j2 = np.eye(5)


#ARRAY DAN MATRIKS KAYA NOLAN DAN SATUAN CUMA ANGKA LAIN
k = np.full((3,3),57)
print (k)



#Matriks random
k1 = np.floor(np.random.rand(3,3)*10) #random banget
k2 = np.random.randint(0,100,(3,3)) #ada min,max,dan shape nya



#Mendeteksi matriks True or False(dengan sebuah kondisi)
l = np.array([[1,2,3,4],[5,6,7,8]])
print (l)
m = l < 3
print (m)
n = l > 3
print (n)



#BUAT MATRIKS YANG SHAPE NYA SAMA DENGAN MATRIKS LAIN, tapi number nya sama semua/random
o = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print (o)
p = np.full((np.shape(o)),39) #cara1
print (p)
q = np.full_like(o, 27) #cara 2
print (q)
#atau mau random
r = np.floor(np.random.random_sample(o.shape)*10)
print (r)



#MEMBUAT ARRAY REPEAT (YANG DIULANG ULANG TERUS ANGKANYA)
s = np.array([[1,2,3],[4,5,6]]) #harus array 2 dimensi
t = np.repeat(s, 3,axis=0)
print (t)



#awas!!! ARRAY YANG SHARING KONTEN
u = np.array([1,2,3,4,5])
v = np.copy(u) #makanya pake copy
print (v)
v[0] = 100
print(v)
print (u)


#3D Array
x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print (x)



# print (a)
# print (b)
# print (c)
# print (d)
# print (e)
# print (f)
# print (g)
# print (h)
# print (i)
# print (j1)
# print (j2)
# print (k1)
# print (k2)
