class mahasiswa():
    __nilai = 0 #private
    jurusan = 'mekatronika' #public
 
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  #public
        self.nim = input_nim #public

    def uts(self, input_nilai):
        self.__nilai += input_nilai
    
    def uas(self, input_nilai):
        self.__nilai += input_nilai
    
    def check_lulus(self):
        if self.__nilai < 50:
            print (self.nama, 'tidak lulus')
        else :
            print (self.nama, 'lulus')
    


otong = mahasiswa('otong surotong', 219341029)
ucup = mahasiswa('michael ucup', 21934030)
# print (otong.nama, otong.nim)


otong.uts(30)
otong.uas(30)
otong.check_lulus()



ucup.uts(20)
ucup.uas(20)
ucup.check_lulus()


