class Hero():
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
    
    @property
    def showInfo(self):
        print ('{} : \n\thealth : {} \n\tattack : {} \n\tarmor : {}'.format(self.name, self.health, self.attack, self.armor))


class Hero_intelligent(Hero):
    def __init__(self, name): #ini yang ditangkep dari definisi sniper bawah
        super().__init__(name,1000,10,5) #ini yang bakal dikirim ke__init__Hero
           
    @property                                     #jadi DEFAULT ini teh
    def showInfo(self):
         print ('{} : \n\ttipe : intelligent \n\thealth : {} \n\tattack : {} \n\tarmor : {}'.format(self.name, self.health, self.attack, self.armor))


sniper = Hero_intelligent ('sniper')
garo = Hero ('garo', 100, 10, 5)


sniper.showInfo
garo.showInfo