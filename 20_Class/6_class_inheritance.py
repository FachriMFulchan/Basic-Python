#INHERITANCE = WARISAN
#jadi class yang dapet informasinya dari class lain
#tapi satu arah aja, bukan berbagi informasi
#informasi itu juga bisa sama bisa juga di ubah\
#kalo di ubah namanya OVERRIDE

class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
    
    def check_id_driver(self):
        print('nama :', self.nama, '\ntransmisi:',self.transmisi,'\ndaerah',self.daerah)


class Gojek(Ojek):
    #nih di override nih, kalo gamau nambah overide pass aja
    def check_id_driver(self):
        print ('Cek aplikasi ya')



ojek1 = Gojek('mario', 'otomatis', 'Bandung')
ojek2 = Ojek('maria', 'manual', 'Zimbabwe')

ojek1.check_id_driver()
ojek2.check_id_driver()



#gaboleh DRY(programnyda diulang ulang) karena ga efektif
#jadinya pake inheritance