#Nomer 1
#+++++++++++0--------5+++++++++8---------11+++++++++++

masuk = float(input('Masukkan angka kurang dari 0 atau antara 5-8 atau lebih dari 11 : '))
print (masuk)

kurangdari0 = masuk < 0
lebihdari11 = masuk > 11

lebihdari5 = masuk > 5
kurangdari8 = masuk < 8
correct1 = lebihdari5 and kurangdari8

correct = kurangdari0 or lebihdari11 or correct1
print ('Apakah angka yang dimasukkan <0 or 5-8 or >11?',correct)
