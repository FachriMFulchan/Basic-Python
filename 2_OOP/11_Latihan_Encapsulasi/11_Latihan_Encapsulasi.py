class Hero:

    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        self.__name = inputName
        self.__healthBase = inputHealth
        self.__attackBase = inputAttack
        self.__armorBase = inputArmor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attack = self.__attackBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax


    @property
    def info(self):
        return '{} level {} : \n\thealth: {}/{} \n\tattack : {} \n\tarmor : {} \n'.format(self.__name, self.__level, self.__health, self.__healthMax, self.__attack, self.__armor)


    @property
    def gainExp (self):
        pass

    @gainExp.setter
    def gainExp (self, addExp):
        self.__exp += addExp

        if self.__exp >= 100:
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attack = self.__attackBase * self.__level
            self.__armor = self.__armorBase * self.__level



sniper = Hero ('sniper', 100, 10, 5)



print (sniper.info)
sniper.gainExp = 110
print (sniper.info)
sniper.gainExp = 110
print (sniper.info)

