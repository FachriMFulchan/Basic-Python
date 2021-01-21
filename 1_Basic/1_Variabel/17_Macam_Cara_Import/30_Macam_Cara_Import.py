#CARA 1, NORMAL
import matematika30
matematika30.tambah(3,4)
matematika30.kurang(3,4)
print('\n')



#CARA 2, nama file nya DIMISALIN biar singkat
import matematika30 as math
math.tambah(3,4)
math.kurang(3,4)
print('\n')



#CARA 3, ngambil spesifik beberapa fungsinya
from matematika30 import tambah,kurang
tambah (9,1)
kurang (9,1)
print('\n')


#CARA 4, kalo mau ngambil semua fungsinya, pake *
from matematika30 import *
tambah (9,1)
kurang (9,1)
print('\n')


#CARA 5, cara ke 3 tapi bisa juga dimisilin biar singkat
from matematika30 import tambah as plus, kurang as subs
plus(8,1)
subs(8,1)

