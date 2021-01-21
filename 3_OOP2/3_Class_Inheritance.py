class Player():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def getName(self) :
        return self.name
    
    def getSpeed(self):
        return self.speed


class ArgentinaPlayer(Player):
    def __init__(self, name, speed,skill):
        Player.__init__(self,name,speed)
        self.freestyle = skill
    
    def getFreestyle(self):
        return self.freestyle

messi = ArgentinaPlayer('messi',100,1000)
print(messi.getName())



