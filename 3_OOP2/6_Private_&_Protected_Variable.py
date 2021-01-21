class Player():
    def __init__(self, name):
        self.name = name
        self.__age = 23

    def getAge(self):
        return dybala.__age

dybala = Player('dybala')
print (dybala.name)
dybala.name = 'huya'
print (dybala.name)
dybala.__age = 25 #gabisa diubah
print (dybala.getAge())


#cara licik
dybala._Player__age = 25 #gausah pake setter
print (dybala.getAge())