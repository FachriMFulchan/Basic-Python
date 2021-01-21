class Hero():
    #class variabel
    jumlah_hero = 0


    def __init__(self, inputNama, inputHealth, inputPower, inputArmor):
        self.name = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    
    #method tanpa argumen dan return
    def siapa(self):
        print ('namaku adalah', self.name)
    
    #method dengan argumen tanpa return
    def healthUp(self,up):
        self.health += up
    
    #method pake return, bisa juga pake argumen
    def getHealth(self):
        return self.health



hero1 = Hero('sniper', 100, 10, 4)
hero2 = Hero('mario bros', 100, 90, 8)


hero1.siapa()
hero1.healthUp(20)
print (hero1.getHealth())
