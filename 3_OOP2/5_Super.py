class Player():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def getName(self):
        return(self.name)
    
    def getSpeed(self):
        return(self.speed)


class ArgentinaPlayer(Player):
    def __init__(self,name):
        super().__init__(name,100)
        print('Hello')


messi = ArgentinaPlayer('messi')
print(messi.name)
print (messi.speed)