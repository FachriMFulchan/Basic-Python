class Hero():

    def __init__(self, inputName, inputHealth, inputAttack):
        self.__name = inputName
        self.__health = inputHealth
        self.__attack = inputAttack
    
    #getter
    def getName (self):
        return self.__name

    def getHealth(self):
        return self.__health

    #setter
    def changeName(self, newName):
        self.__name = newName

    def diserang (self, keserang):
        self.__health -= keserang



sniper = Hero('sniper', 100, 10)


print(sniper.getName())
print(sniper.getHealth())

sniper.changeName('Zilong')
print(sniper.getName())

sniper.diserang(10)
print(sniper.getHealth())




#jadi memanngil atau merubah atributnya lewat
#FUNGSI