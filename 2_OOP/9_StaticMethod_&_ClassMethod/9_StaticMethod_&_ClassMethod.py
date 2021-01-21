#terus gimana getter dan setter buat private class variabel

class Hero():
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1
    
    #cuma berlaku buat objek
    def getJumlah (self):
        return Hero.__jumlah


    # #self nya diilangin, cuma berlaku buat class, tapi problem
    # def getJumlah2():
    #     return Hero.__jumlah


    #gimana kalo bisa berlaku kedua duanya, pake static method
    @staticmethod
    def getJumlah3():
        return Hero.__jumlah

    
    def getJumlah4(self):
        return self.__jumlah


sniper = Hero('sniper')
print (sniper.getJumlah4())

rikimaru = Hero('rikimaru')


boa = Hero('boa')


