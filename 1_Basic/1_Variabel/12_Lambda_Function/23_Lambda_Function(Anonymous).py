def jumlah (a,b):
    c = a + b
    return c

hasil = jumlah(4,5)
print (hasil)


#kita juga bisa membuat fungsi dengan lambda
#lambda adalah fungsi yang tidak mempunyai nama
#dengan begitu dibutuhkan variabel untuk menyimpannya
# dan ini merupakan kelebihan lambda
#karena fungsi biasa tidak bisa disimpan ke dalam variabel

#lambda : parameter, expression
#parameter nya boleh banyak, tapi ekspresi nya cuma boleh satu
#dan lambda ini BISA LANGSUNG DI EKSEKUSI, gausah DIPANGGIL


greeting = lambda name: print('Hai', name)
greeting ('Fachri')
greeting ('Joni')

sapa = greeting #bisa dipindah pindah
sapa ('Zahra')

hasil = (lambda x,y: x*2 + y*2)(4,6) #gausah dipanggil, lebih simple gausah return return
print (hasil)


kali = lambda x,y: x*y
print (kali(3,4)) #bisa gini, DIPANGGIL

kali = (lambda x,y: print(x*y))(3,4) #bisa juga gini, LANGSUNG


#ADVANCE
bilangan = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, bilangan) 
print(list(filtered_result))

