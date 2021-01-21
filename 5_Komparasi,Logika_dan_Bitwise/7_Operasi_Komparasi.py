#Operasi Komparasi
#setiap hasi dari operasi komparasi adalah boolean
#>, <, <=, >=, ==, !=, is, is not

a = 4
b = 2

#lebih besar dari >
print ('=========== lebih besar dari (>)')
hasil = a > 3
print (a, '>', 3, '=', hasil)
hasil = b > 3
print (b, '>', 3, '=', hasil)
hasil = b > 2
print (b, '>', 2, '=', hasil)

#kurang dari <
print ('=========== kurang dari (<)')
hasil = a < 3
print (a, '<', 3, '=', hasil)
hasil = b < 3
print (b, '<', 3, '=', hasil)
hasil = b < 2
print (b, '<', 2, '=', hasil)

#lebih dari sama dengan >=
print ('=========== lebih dari sama dengan  (<)')
hasil = a >= 3
print (a, '>=', 3, '=', hasil)
hasil = b >= 3
print (b, '>=', 3, '=', hasil)
hasil = b >= 2
print (b, '>=', 2, '=', hasil)

#kurang dari sama dengan >=
print ('=========== kurang dari sama dengan (<)')
hasil = a <= 3
print (a, '<=', 3, '=', hasil)
hasil = b <= 3
print (b, '<=', 3, '=', hasil)
hasil = b <= 2
print (b, '<=', 2, '=', hasil)

#sama dengan =
print ('=========== sama dengan (=)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

#tidak sama dengan !=
print ('=========== tidak sama dengan (!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# is sebagai komparasi objek (object identity)
print ('=========== Object identity is (!=)')
x = 5
y = 5
print ('nilai x =', x, 'id = ', hex (id(x)))
print ('nilai y =', y, 'id = ', hex (id(y)))
#walaupun variabel nya beda, tapi isinya sama bakal ditaro di
#memori yang sama, PYTHON PINTER BANGET IH
hasil = x is y
print ('x is y =',hasil)

#is not
print ('=========== Object identity is not (!=)')
x = 5
y = 6
print ('nilai x =', x, 'id = ', hex (id(x)))
print ('nilai y =', y, 'id = ', hex (id(y)))
hasil = x is not y
print ('x is not y =',hasil)