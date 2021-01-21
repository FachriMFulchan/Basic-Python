class Hero ():
    
    def __init__(self, inputName, inputHealth, attackPower, armorNumber):
        self.name = inputName
        self.health = inputHealth
        self.attack = attackPower
        self.armor = armorNumber
    
    def menyerang (self, lawan):
        print (self.name, 'menyerang', lawan.name) 
        lawan.diserang(self, self.attack) 

    def diserang (self, lawan, attack_lawan): 
        print (self.name, 'diserang', lawan.name)
        
        get_attack = attack_lawan/self.armor
        print ('Attack yang diterima: ', get_attack)

        self.health -= get_attack
        print ('Darah dari', self.name, 'tersisa', self.health)
    






sniper = Hero ('sniper',100, 20, 5)
rikimaru = Hero ('rikimaru', 100, 5, 10)

sniper.menyerang(rikimaru)
print ('\n')
sniper.menyerang(rikimaru)
print ('\n')
sniper.menyerang(rikimaru)
print ('\n')
sniper.menyerang(rikimaru)
print ('\n')
sniper.menyerang(rikimaru)
print ('\n')
sniper.menyerang(rikimaru)
print ('\n')
sniper.menyerang(rikimaru)
print ('\n')
sniper.menyerang(rikimaru)
print ('\n')