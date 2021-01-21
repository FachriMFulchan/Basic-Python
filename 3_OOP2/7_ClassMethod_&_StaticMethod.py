class Player():
    job = 'pemain bola'

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    @staticmethod
    def retiredIn (age):
        return 40 - age

    @classmethod
    def generalInfo (cls, age):
        return (cls.job, 'ini akan pensiun dalam', cls.retiredIn(age),'tahun')
    

print(Player.retiredIn(30))
print(Player.generalInfo(19))
