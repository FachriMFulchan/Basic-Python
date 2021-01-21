#biar simple untuk masukin datanya daripada yang sebelumnya
#maka kita pakai init
#bukan init untuk bikin package ya, tapi fungsinya mirip
#sebagai inisiasi

class mahasiswa():
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.nim = input_nim
    
    def belajar(self,kondisi):
        print (self.nama, 'sedang belajar', kondisi)



otong = mahasiswa('otong surotong', 219341029)
ucup = mahasiswa('ucup gambut', 219341039)

print(otong.nama)
print(otong.nim)
print(ucup.nama)
print(ucup.nim)
otong.belajar('dengan giat')


#tapi kalo kaya gini masih bisa diganti ganti dengan mudah
#bisa di HACK lah dengan mudah

