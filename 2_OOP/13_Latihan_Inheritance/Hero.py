class Hero():
    def __init__(self, name):
        self.__health_pool = [0,100,200,300,400,500]
        self.__attack_pool = [0,10,20,30,40,50]
        self.__armor_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level = 1

        self.__health = self.__health_pool [self.__level]
        self.__attack = self.__attack_pool [self.__level]
        self.__armor = self.__armor_pool [self.__level]



    def show_info(self):
        print ('{} level {} \n\thealth : {} \n\tattack : {} \n\tarmor : {}'.format(
                self.__name,
                self.__level,
                self.__health,
                self.__attack,
                self.__armor
        )
    )

    @property
    def gainExp (self) :
        pass

    @property
    def levelUp (self):
        pass

    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input

        if self.__exp >= 100 :
            self.levelUp = self.__exp // 100
            self.__exp %= 100
    
    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__health_pool [self.__level]
        self.__attack = self.__attack_pool [self.__level]
        self.__armor = self.__armor_pool [self.__level]
        
    @property
    def newHealth_pool (self):
        pass

    @property
    def newAttack_pool (self):
        pass

    @property
    def newArmor_pool (self):
        pass


    @newHealth_pool.setter
    def newHealth_pool (self, input):
        self.__health_pool = input

    @newAttack_pool.setter
    def newAttack_pool (self, input):
        self.__attack_pool = input

    @newArmor_pool.setter
    def newArmor_pool (self, input):
        self.__armor_pool = input

    def getHealth(self):
        return self.__health_pool 



class Hero_intelligence (Hero):
    def __init__(self, name):
        super().__init__(name)
        self.newHealth_pool = [0,50,100,150,200,250]
        self.newAttack_pool = [0,20,40,60,80,100]
        self.newArmor_pool = [0,0.5,1,1.5,2,2.5]
        self.levelUp = 0


class Hero_strenght (Hero):
    def __init__(self, name):
        super().__init__(name)
        self.newHealth_pool = [0,200,400,600,800,1050]
        self.newAttack_pool = [0,10,20,30,40,50]
        self.newArmor_pool = [0,0.5,1,1.5,2,2.5]
        self.levelUp = 0


