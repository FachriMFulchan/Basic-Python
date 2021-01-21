class Hero:

    def __init__(self, inputNama, inputHealth, inputArmor):
        self.__name = inputNama
        self.__health = inputHealth
        self.__armor = inputArmor

    @property
    def armor(self):
        pass

    @armor.getter  #ngambil
    def armor (self):
        return self.__armor
    
    @armor.setter #ngubah
    def armor(self, input):
        self.__armor = input

    @armor.deleter #delete
    def armor(self):
        self.__armor = None



sniper = Hero('sniper', 100, 10)



print(sniper.armor)

sniper.armor = 250
print(sniper.armor)

del sniper.armor
print (sniper.armor)


#jadi simpel pemanggilannya
#kenapa gapake variabel public dari awal??????
