class Hero(): #template
    #Class Variabel
    jumlah = 0

    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        #Objek Variable/Atribut
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print('membuat hero yang bernama', inputName)
        print (Hero.jumlah)


hero1 = Hero('sniper', 100, 10, 4)
hero2 = Hero('sven', 100, 15, 1)
hero3 = Hero('ucup', 1000, 100, 0)
