'''BISA JUGA GINI
LEBIH SINGKAT
JADI KALO MISAL NAMA KELASNYA DIUBAH
GAUSAH GANTI GANTI LAGI'''

class Hero():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print ('{} dengan health: {}'.format(self.name, self.health))



class Hero_tanker (Hero):
    def __init__(self, name):
        super().__init__(name,100)
        super().showInfo()

class Hero_MM (Hero) :
    def __init__(self,name):
        super().__init__(name, 200)


lani = Hero_tanker('Lani')
couch = Hero_MM ('Couch')

print (lani.name, '', lani.health)
print (couch.name, '', couch.health)



'''KALO DI SUPERCLASS NYA ADA PRESET (ANGKA TETAP)
KALO MAU DIGANTI HARUS PAKE METHOD
'''