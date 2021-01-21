import numpy as np


#membuat matriks dengan tipe data tertentu
a = np.array(((1,2,3),(4,5,6)), dtype = bool)
# print (a)


#membuat array dengan fungsi
def kuadrat (baris, kolom):
    return kolom ** 2

b = np.fromfunction(kuadrat, (5,5), dtype = int)
print (b)



def jumlah (baris, kolom):
    return (baris + kolom)

c = np.fromfunction(jumlah, (4,4), dtype = float)
print (c)

''' mirip sandi GUDEP SEDIA '''


#membuat array dengan iterable
iterable = ( x*2 for x in range (5))

d = np.fromiter(iterable, dtype = int)

print (d)



#multiple array
#jadi dalem nya bisa string bisa int, dll

data = [
        ('ucup', 150),
        ('otong', 160),
        ('mario', 170)
        ]

dtipe = [('nama', 'S255'),('tinggi', int)]

e = np.array(data, dtype = dtipe)
print (e)
#LUAR BIASA INI GANGERTI