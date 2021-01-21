#Latihan Komparasi dan Logika

#Program mendeteksi angka yang kurang dari 3 atau lebih dari 10
#kalo diantara itu berarti false
#+++++++++++++3----------10+++++++++

masuk = float(input('Masukkan angka yang kurang dari 3 atau lebih dari 10: '))

kurangdari3 = (masuk < 3)
print ('Kurang dari 3 : ', kurangdari3)

lebihdari10 = (masuk > 10)
print ('Lebih dari 10 : ',lebihdari10)

correct = kurangdari3 or lebihdari10
print ('angka yang dimasukkan : ',correct)
print ('\n')


#Program mendeteksi kalo diantara 3 dan 10 berarti True
#--------3++++++++10--------
#irisan

masuk = float(input('Masukkan angka yang kurang dari 3 atau lebih dari 10: '))

lebihdari3 = (masuk > 3)
print ('Lebih dari 3 :', lebihdari3)

kurangdari10 = (masuk < 10)
print ('Kurang dari 10:', kurangdari10)

correct = lebihdari3 and kurangdari10
print ('angka yang dimasukkan : ',correct)
