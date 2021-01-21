class Hero:

    def __init__(self, inputName, inputHealth, inputArmor):
        self.__name = inputName
        self.__health = inputHealth
        self.__armor = inputArmor
        # self.__info = 'name : {} \nhealth : {}'.format(self.__name, self.__health)


    #setter
    def changeName(self,newName):
        self.__name = newName

    @property
    def info(self):
        return 'name : {} \nhealth : {}'.format(self.__name, self.__health)





sniper = Hero('sniper', 100, 10)


print (sniper.info)
sniper.changeName('Zilong')
print (sniper.info)

