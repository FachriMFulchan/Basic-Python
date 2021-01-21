class Player ():
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

class BrazilPlayer(Player):
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

pele = BrazilPlayer('pele',70)
print(pele.name)
print(pele.speed)
pele.setAge(771)
print(pele.getAge())