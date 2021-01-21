class Hero:

    def __init__(self, inputNama, inputHealth, inputArmor):
        self.__name = inputNama
        self.__health = inputHealth
        self.__armor = inputArmor
    
    #getter
    def getArmor (self) :
        return self.__armor

    #setter
    def changeArmor(self, input):
        self.__armor = input



sniper = Hero('sniper', 100, 10)


print (sniper.getArmor())
sniper.changeArmor(100)
print (sniper.getArmor())

