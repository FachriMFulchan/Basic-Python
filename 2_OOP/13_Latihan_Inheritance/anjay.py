class Hero():
    def __init__(self, name):
        self.__health_pool = [0,100,200,300,400,500]

    @property
    def newHealth_pool (self):
        pass

    @newHealth_pool.setter
    def newHealth_pool (self, input):
        self.__health_pool = input
    

    def getHealth(self):
        return self.__health_pool


class Hero_intelligence (Hero):
    def __init__(self, name):
        super().__init__(name)
        self.newHealth_pool = [0,50,100,150,200,250]

garo = Hero_intelligence('garo')

print (garo.getHealth())