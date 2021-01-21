class Player():
    job = 'pemain bola'


    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    @staticmethod
    def retiredIn(age):
        return 40-age
    

    @classmethod
    def generalInfo(cls):
        return (cls.job +'akan pensiun dalam ' + str(cls.retiredIn(19)) + ' tahun')


print (Player.generalInfo())


