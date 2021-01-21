class pegawai():

    jumlah_pegawai = 0

    def __init__(self,input_nama, input_pekerjaan):
        self.nama = input_nama
        self.pekerjaan = input_pekerjaan
        pegawai.jumlah_pegawai += 1



jajar = pegawai('jajar ali', 'engineer')
seno = pegawai('seno roseno', 'programmer')
agnes = pegawai('agnes mokawin', 'penyanyi')

print (pegawai.jumlah_pegawai)