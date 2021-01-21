#Input User

#data yang dimasukin otomatis kebacanya string
data = input('Masukkan data: ')
print ('data :',data, 'type : ',type(data))

#kalo mau int, maka kita casting
data_int = int(input ('Masukkan angka: '))
print ('data :',data_int, 'type : ',type(data_int))

#kalo mau float
data_float = float(input ('Masukkan angka: '))
print ('data :',data_float, 'type : ',type(data_float))

#kalo mau biner/bool
#ubah dulu ke int, baru ke bool
#kalo ga dipindahin dulu semuanya bakal kebaca True karna dari string
biner = bool(int(input('Masukkan nilai boolean :')))
print ('data :',biner, 'type : ',type(biner))
