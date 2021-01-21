'''Variabel kan di private sama kita biar gabisa diubah sama orang lain
sebenernya masih bisa kita panggil ke luar class dan diubah
dengan cara GETTER dan SETTER
bikin fungsi aja yang nge RETURN nilai private nya
terus panggil fungsinya
'''

class Hero():

    def __init__(self, inputName, inputHealth, inputAttack):
        self.__name = inputName
        self.__health = inputHealth
        self.__attack = inputAttack
    


    #getter
    def menyerang (self, lawan):
        print (self.__name, 'menyerang', lawan.__name)
        lawan.diserang(self)

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health
    



    #setter
    def diserang(self, lawan):
        print (self.__name, 'diserang', lawan.__name)
        self.__health -= lawan.__attack
        print (self.__name, 'health tersisa', self.__health)







earthshaker = Hero('earthshaker', 50, 5)
sniper = Hero('sniper', 70,2)


earthshaker.menyerang(sniper)
print(sniper.getHealth())
