class Hero():
    def __init__(self, name):
        self.__health_pool = [0,100,200,300,400,500]
        self.__attack_pool = [0,10,20,30,40,50]
        self.__armor_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level = 0



    def show_info (self):
        print ('{} level {} \n\thealth : {} \n\tattack : {} \n\tarmor : {}'.format(
                self.__name,
                self.__level,
                self.__health,
                self.__attack,
                self.__armor
        )
    )


    @property
    def health_pool(self):
        pass

    @property
    def attack_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def gainExp(self):
        pass

    @property
    def levelUp(self):
        pass


    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input

        if self.__exp >= 100:
            self.levelUp = self.__exp // 100
            self.__exp %= 100
    

    @levelUp.setter
    def levelUp (self, input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attack = self.__attack_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        





sniper = Hero('sniper')

sniper.levelUp = 1
sniper.show_info()
sniper.gainExp = 301
sniper.show_info()

