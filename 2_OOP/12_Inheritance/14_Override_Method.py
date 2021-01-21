'''kalo ada method yang sama di superclass dan subclass
maka salah satu akan di override
biasanya sih yang superclasss'''


class Hero():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def showInfo (self):
        print ('{} \n\thealth: {}'.format(self.name, self.health))

class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    #overide
    def showInfo(self):
        print ('{} \n\ttipe : intelligent \n\thealth : {}'.format(self.name, self.health))
        

class Hero_strenght(Hero):
    def __init__(self,name):
        super().__init__(name, 200)

    #ga di override da gaada yang sama


lina = Hero_intelligent('lina')
axe = Hero_strenght ('axe')

lina.showInfo()
axe.showInfo()