'''nah disini ad interaksi antar object nih
cermatin soalnya keren
INTINYA gini, selain kita bisa ngasih argument berupa ANGKA sama TEXT
kita juga bisa ngasih OBJECT sebagai ARGUMENT
'''

class Hero ():
    
    def __init__(self, inputName, health, attackPower, armorNumber):
        self.name = inputName
        self.attack = attackPower
        self.armor = armorNumber
    
    def menyerang (self, lawan):
        print (self.name, 'menyerang', lawan.name) #ngeprintnya lawan.name karena lawan kan objek
        lawan.diserang(self) #lawan manggil diserang

    def diserang (self, lawan): #disini self&lawan nya kebalikan sama yang menyerang
        print (self.name, 'diserang', lawan.name)
    

sniper = Hero ('sniper',100, 10, 5)
rikimaru = Hero ('rikimaru', 100, 5, 10)

sniper.menyerang(rikimaru)  #nah rikimaru tuh objek dijadiin argumen