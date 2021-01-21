class Player():

    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    
    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed



ronaldo = Player('ronaldo',1000)
messi = Player('messi',101)

print (ronaldo.name,'mempunyai speed',ronaldo.speed)
print (messi.name,'mempunyai speed',messi.speed)