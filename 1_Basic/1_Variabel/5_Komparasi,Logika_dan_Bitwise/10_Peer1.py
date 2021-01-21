#Nomer 1
#--------0++++++++=5-------8+++++++11--------

masuk = float(input('Masukkan angka antara 0-5 atau 8-11: '))
print (masuk)

#0-5
lebihdari0 = masuk > 0

kurangdari5 = masuk < 5

correct1 = lebihdari0 and kurangdari5
print ('Angkanya antara 0-5?', correct1)


#8-11
lebihdari8 = masuk > 8

kurangdari11 = masuk < 11

correct2 = lebihdari8 and kurangdari11
print ('Angkanya antara 8-11?', correct2)


#Or-in
correct = correct1 or correct2
print ('Apakah angka yang dimasukkan antara 0-5 atau 8-11?', correct)

