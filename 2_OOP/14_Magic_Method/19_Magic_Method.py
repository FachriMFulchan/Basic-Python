#magic method

class Mangga():

    def __init__(self, name, jumlah): #akan tereksekusi jika kita manggil kelasnya
        self.name = name
        self.jumlah = jumlah

    def __repr__(self):
        return 'Debug - Mangga : {}, dengan jumlah : {}'.format(self.name, self.jumlah)
        #bakal muncul kalo manggil objek, daripada muncul alamat ya kan gajelas, mending muncul ini

    def __str__(self):
        return 'Mangga : {}, dengan jumlah : {}'.format(self.name, self.jumlah)
        #SAMA AJA KAYA REPR
        #cuma inimah kalo programnya dah jadi
        #kalo repr buat debugging
    
    def __add__(self, objek):
        return self.jumlah + objek.jumlah 
        #buat nambah
    
    @property
    def __dict__(self):
        return 'objek ini mempunyai nama dan jumlah'
        #harus pake properti

belanja1 = Mangga('arummanis', 10)
belanja2 = Mangga('gincu', 30)
print (repr(belanja1))
print (belanja2)
print(belanja1 + belanja2)
print (belanja1.__dict__)

#tanda magic method ada __