#input output file
#jadi nulis di python nanti muncul di .txt
#atau txt dibaca sama python

#ada 4 mode
'''
w = write mode/mode menulis dan mengapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambah data diakhir baris (tidak menghapus data yang sebelumnya)
r+ = write and read mode
'''

#membuat file text
file = open('data.txt','w')

file.write('ini adalah text yang dibuat menggunakan python')
file.write('\nini baris kedua')
file.write('\nini baris ketiga')
file.write('\nini baris keempat')

file.close()


#membaca file text
file2 = open('data.txt', 'r')


print (file2.read())
# print (file2.readline)

file2.close()


#appending mode
file3 = open ('data.txt', 'a')

file3.write('\nbaris ini dibuat digunakan mode appaend')



# #read and write mode
# file4 = open ('data.txt', 'r+')

# file4.write('\nbaris baru nih hayuuuuuuuu')
# print(file4.read())