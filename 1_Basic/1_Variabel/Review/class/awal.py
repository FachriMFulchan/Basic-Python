class mahasiswa():
    __nilai = 0
    
    def __init__(self, input_nama, input_kelas):
        self.nama = input_nama
        self.kelas = input_kelas

    def uts (self, input_nilai):
        self.__nilai += input_nilai
    
    def uas (self, input_nilai):
        self.__nilai += input_nilai
    
    def check_status(self):
        if self.__nilai < 50:
            print (self.nama, 'tidak lulus')
    
        else:
            print (self.nama, 'lulus')




otong = mahasiswa('Otong Surotong', '1AEB')

otong.uts(30)
otong.uas(30)
# print(otong.nilai)
otong.check_status()