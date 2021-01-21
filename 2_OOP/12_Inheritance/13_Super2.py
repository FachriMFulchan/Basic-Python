class Hero():
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero_Intelligence(Hero):
    def __init__(self, name):
        Hero.__init__(self,name, 100) #panggil initnya si class Hero


class Hero_Strenght(Hero):
    def __init__(self, name):
        Hero.__init__(self,name,200)


lina = Hero_Intelligence('lina')
axe = Hero_Strenght('axe')


print (lina.name, '', lina.health)
print (axe.name, '', axe.health)


'''jadi class yang merupakan warisan dari class lain
TAPI MAU ADA NILAI DEFAULTNYA JUGA
'''