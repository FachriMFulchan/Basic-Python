#Merubah List dengan Slicing
print('Merubah Data dengan Slicing')
Data = [1,4,9,25,36,49,64]
print (Data)
Data[3:5] = [11,12]
print (Data)
print ('\n')


#List dalam List
print ('List dalam List')
Data = [1,4,9,25,36,49,64]
Data2 = [100,200,300,400,500]
Data3 = [Data,Data2]
print (Data3)

#Ngaksesnya
print(Data3[0][3])
print(Data3[1][4])
print('\n')



#Metode List(Append, menambah ke konten paling belakang)
print ('Metode List(append)')
Data = [1,4,9,25,36,49,64]
Data.append(30)
print (Data)

Data2 = [100,200,300,400,500]
Data.append(Data2)
print (Data)
print ('\n')

#Menghitung banyak nya data dalam list dengan len
print ('Fungsi Panjang Data (len)')
Data = [1,4,9,25,36,49,64]
print ('Banyaknya Data pada Variable Data: ',len(Data))
