class Hero():
    def __init__(self, name, health):
        self.name = name
        self.health = 500

    def changeHealth(self,input):
        self.health = input

    
class Hero_intelligence(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 2000)
        self.changeHealth([0,10,20])

sniper = Hero_intelligence('sniper')


print (sniper.name)
print (sniper.health)