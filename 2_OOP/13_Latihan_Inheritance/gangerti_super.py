class mahasiswa():
    def __init__(self, nama, nim, absen, kelas):
        self.nama = nama
        self.nim = nim
        self.absen = absen
        self.kelas = 0
        self.tinggi = 180


class mahpolman(mahasiswa):
    def __init__(self, nama):
        super().__init__(nama, 219,14,'1aeb')

fachri = mahpolman('fachri')

print (fachri.absen)
print (fachri.kelas)
print (fachri.tinggi)