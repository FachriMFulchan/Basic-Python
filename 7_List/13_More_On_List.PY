#Beberapa metode tambahan yang bisa diterapin di list
barang =['kunci', 'ember', 'jaket', 'ban', 'mobil']
print (barang)

#Metode untuk menambah konten list
barang.append('sepeda')  #menambah dari belakang
print (barang)

barang.extend('dompet')  #menambah tapi dipisah
print (barang)

barang.insert(3, 'sepeda')  #menambah pada indeks tertentu
print (barang)



#Metode untuk menghitung list
hitung = barang.count('sepeda')  #menghitung konten tertentu dalam list, biasanya kan pake looping looping gituh
print ('banyaknya sepeda adalah ', hitung, 'buah')


#Metode untuk menghapus konten list
barang.remove('sepeda')
print(barang)

#Metode untuk membalik kedudukan konten dalam list
barang.reverse()
print (barang)


#biar ga sharing konten, stuff itu mengcopy barang, bukan ganti nama doang
stuff = barang.copy()
stuff.append('gelas')
print (stuff)
print (barang)