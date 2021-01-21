import numpy as np

a = np.arange(10)**2
print (a)


#mengambil nilai (indexing)
print ('elemen ke-1 dari a adalah : ',a[0])
print ('elemen ke-7 dari a adalah : ',a[6])
print ('elemen ke-akhir dari a adalah : ',a[-1])

#slicing
print ('elemen dari 1-6 adalah : ', a[0:6])
print ('elemen dari 4 sampe akhir adalah : ', a[3:])
print ('elemen dari awal sampe 5 adalah : ', a[:5])

#iterasi
for i in a :
    print ('value : ', i)



b = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print (b)

#akses spesifik elemen
print (b[0,3])
print (b[0][3]) #same thing


#akses specific kolom
print (b[:,2])


#akses specific baris
print (b[1,:])


#slice data tapi step
print (b[0,1:-1:2])


#replace or change data
b[0,1] = 100
print (b)

b[:,1] = [200,201]
print (b)



#Akses 3D Array
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print (c)
print(c[0,1,1])
c[:,1,:] = [100,200],[300,400]
print (c)



#ADVANCE
#SLICING DENGAN MENGGUNAKAN LIST
a = np.array([1,2,3,4,5,6,7,8,9])
print (a[[0,1,2]])  #jadi langsung keambil nilai mana aja yang mau diambil