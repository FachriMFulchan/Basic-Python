class Player():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def skill(self):
        return 'normal'


class ArgentinaPlayer(Player):
    def skill(self):
        return 'cepat'

class BrazilPlayer(Player):
    pass


messi = ArgentinaPlayer('messi',98)
print(messi.skill())

ronaldinho = BrazilPlayer('ronaldinho',40)
print (ronaldinho.skill())
