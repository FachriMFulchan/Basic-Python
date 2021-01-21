'''KELEBIHAN MAKE PROPERTI ADALAH
DATANYA SELALU APDET
GINI NIH CONTOHNYA
'''

class Hero:

    def __init__(self, inputName, inputHealth, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor
        self.info = 'name : {} \nhealth : {}'.format(self.name, self.health)
    


sniper = Hero('sniper', 100, 10)

print (sniper.info)
sniper.name = 'dadang'
print (sniper.info)
print ('\n')

'''walaupun sniper.name nya udh diubah tapi si sniper.info nya ga apdet
KENAPA??? karena self.info cuma sekali aja ASSIGNMENT NYA
TERUS GA DIMASUK MASUKKIN. TERUS GIMANA???
dilanjut di update 2
'''

