'''MISALKAN di kelas yang diwariskannya mau ada nilai DEFAULT
gini caranya'''

class Hero():
    def __init__ (self, name, health):
        self.name = name
        self.health = health


class Hero_intelligent(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 100
        

class Hero_strenght(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 200

'''tapi kalo gini kan NGULANG
DI PEMROGRAMAN KITA TUH GABOLEH NGULANG PROGRAM
JADI GIMANA???'''


lina = Hero_intelligent('lina')
axe = Hero_strenght('axe')

print (lina.name, '', lina.health)
print (axe.name, '', axe.health)
print (axe.__dict__)