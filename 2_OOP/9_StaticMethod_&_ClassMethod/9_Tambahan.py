class Hero:

    #private class variable
    __jumlah = 0

    def __init__(self, inputName):
        self.name = inputName
        Hero.__jumlah += 1
    

    #method ini hanya berlaku untuk objek
    def getJumlah (self):
        return Hero.__jumlah


    # #method ini tidak berlaku untuk objek tapi berlaku untuk class
    # def getJumlah1 ():
    #     return Hero.__jumlah
   


    #buat manggilnya bisa ga, pake class bisa pake objek bisa
    #STATIC METHOD (DECORATOR)
    @staticmethod
    def getJumlah2 ():
        return Hero.__jumlah
    

    #class method sama aja tapi harus pake argumen
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah



sniper = Hero('sniper')
print (Hero.getJumlah2())


rikimaru = Hero('rikimaru')
print (sniper.getJumlah2())


zilong = Hero ('zilong')
print (zilong.getJumlah3())
print (Hero.getJumlah3())