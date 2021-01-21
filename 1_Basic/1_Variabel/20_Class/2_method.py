#classnya
class mahasiswa():
    nama = ''

    def belajar(self, kondisi):
        print (self.nama, 'sedang belajar', kondisi)
    
    def tidur(self, kondisi):
        print (self.nama, 'sedang tidur di kelas', kondisi)
    
    def ngitung(self,a,b):
        print (self.nama, 'berkata bahwa', a,'+',b,'hasilnya adalah')
        return a + b



#main programnya
otong = mahasiswa()
ucup = mahasiswa()

otong.nama = 'otong surotong'
ucup.nama = 'michael ucup'


otong.belajar('dengan giat')
ucup.tidur('nyenyak banget')
ucup.ngitung(5,4)
print (ucup.ngitung(5,4))

#tapi kendalanya kalo mahasiswa nya seratus gimana
#harus nge assign = mahasiswa() satu satu, terus namanya satu satu
#jangan khawatir ada __init__
