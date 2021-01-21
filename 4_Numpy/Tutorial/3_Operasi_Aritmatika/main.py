import numpy as np
'''ELEMENTWISE OPERATION
jadi numpy itu operasi nya per elemen, ga kaya list
'''

#list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])


#penjumlahan
hasil = a + b
print (hasil)

hasil = anp + bnp
print (hasil)



#pengurangan
hasil = anp - bnp
print (hasil)


#perkalian
hasil = anp * bnp
print (hasil)



#pembagian
hasil = anp / bnp
print (hasil)


#kuadrat
hasil = anp ** 2
print (hasil)


#sisa bagi
hasil = bnp % anp
print (hasil)

#etc.


#multidimensi array
c = np.array([(1,2,3), (4,5,6)])
d = np.array([(7,8,9), (-1,-2,-3)])

hasil = c + d
print (hasil)

hasil = c * d
print (hasil)
'''nah disini tuh bukan PERKALIAN MATRIKS
tapi perkalian elementwise operation
PERKALIAN MATRIKS NANTI BEDA LAGI
'''