#Operasi Aritmatika
a = 10
b = 3

#operasi tambah
hasil = a + b
print (a, '+', b, '=', hasil)

#operasi pengurangan
hasil = a - b
print (a, '-', b, '=', hasil)

#Operasi Perkalian
hasil = a * b
print (a, '*', b, '=', hasil)

#Operasi Pembagian
hasil = a / b
print (a, '/', b, '=', hasil)

#operasi exponen (pangkat)
hasil = a ** b
print (a, '**', b, '=', hasil)

#operasi modulus (sisa bagi)
hasil = a % b
print (a, '%', b, '=', hasil)

#operasi floor division (pembagian dibulatkan kebawah)
hasil = a // b
print (a, '//', b, '=', hasil)


#PRIORITAS OPERASI, OPERATIONAL PRECEDENCE
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-', y,'%',z,'//',x,'=', hasil)
'''Jadi prioritasnya tuh dari
1.() , yang dalam kurung
2.Exponen,
3.Perkalian, termasuk pembagian, modulus, dan floor division
4.Pertambahan dan pengurangan'''

hasil = x + y * z
print (x,'+',y,'*',z,'=',hasil) 

hasil =( x + y )* z
print ('(',x,'+',y,')','*',z,'=',hasil) 

