class Player():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def infoPlayer(self):
        pass
    
    @infoPlayer.setter
    def infoPlayer(self,data):
        name, age = data.split(' ')
        self.name = name
        self.age = age
    
    @infoPlayer.getter
    def infoPlayer(self):
        return (self.name + ' berumur ' + str(self.age) + ' tahun')


dybala = Player('Dybala', 24)
print (dybala.infoPlayer)
dybala.infoPlayer = 'PauloDybala 24'
print (dybala.infoPlayer)
