'''STATIC METHOD intinya untuk manggil method yang ada di dalem CLASS
tanpa harus ngedeklarasiin objeknya dulu'''

'''CLASS METHOD intinya dapet ngambil apapun yang ada di dalem class
selama bukan milik objek(self self an)
contoh : STATIC METHOD, CLASS VARIABLE'''

class Hero():
    job = 'menyerang'

    def __init__ (self,name, health):
        self.name = name
        self.health = health
    
    @staticmethod
    def infoGame(versi):
        return 'dota '+str(versi)
    
    @classmethod
    def getJob(cls,kondisi):
        return ('Hero kerjaannya ' + cls.job + ' di '+cls.infoGame(5)+kondisi)


print(Hero.infoGame(5))
print(Hero.getJob(' barbar'))

