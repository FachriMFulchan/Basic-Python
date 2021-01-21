'''KEGUNAAN PROPERTI
SELALU APDET'''

class Hero:
    
    def __init__(self, inputName, inputHealth , inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor
        # self.info = 'nama : {} \nhealth : {}'.format(self.name,self.health)
    
    @property
    def info(self):
        return 'nama : {} \nhealth : {}'.format(self.name,self.health)


sniper = Hero('sniper', 100, 10)



print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

#kalo infonya di __init__ mah gaakan ke APDET APDET ATEUHHH
'''INTINYA KALO PAKE PROPERTY BISA APDET
DAN BISA JUGA DIPAKE DI PRIVAT, SOK COBAIN
''''