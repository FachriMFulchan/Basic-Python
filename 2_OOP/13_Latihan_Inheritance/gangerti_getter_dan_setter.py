class mahasiswa ():
    def __init__(self, name, nim, kelas):
        self.__name = name
        self.__nim = nim
        self.__kelas = kelas
        self.__tinggi_pool = [160,165,170,175,180]


    def show_info(self):
        print ('name ; {} \nnim : {} \nkelas : {} \ntinggi : {}'.format(
            self.__name, 
            self.__nim, 
            self.__kelas,
            self.__tinggi
            )
        )

    def show_tinggi(self, indeks):
        self.__tinggi = self.__tinggi_pool[indeks]
    
    def getTinggi(self):
        return self.__tinggi


fachri = mahasiswa('Fachri', 219, '1AEB')


fachri.show_tinggi(2)
print (fachri.getTinggi())
fachri.show_info()