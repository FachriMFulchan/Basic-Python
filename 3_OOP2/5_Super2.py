class Player():
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    

class BrazilPlayer(Player):
    def __init__(self, name,speed):
        super().__init__(name,speed)


messi = BrazilPlayer('messi', 200)
print (messi.name)
print (messi.speed)