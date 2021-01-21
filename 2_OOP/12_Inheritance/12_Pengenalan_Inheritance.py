'''Inheritance = pewarisan
berlaku antar class ke class
yang satu namanya SUPER CLASS, satu lagi SUBCLASS

jadi misal sebuah class tuh sebagian besar sifatnya sama
sama kelas lain yaudah variabel dan method nya samain aja
dengan cara PEWARISANN
misal: Hero --- Hero Intelligence, Hero Strenght
'''


class Hero():

    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero_Intelligence(Hero):
    pass

class Hero_Strenght(Hero):
    pass


lina = Hero('lina', 100)
goro = Hero_Intelligence ('goro', 100)
cowny = Hero_Strenght ('cowny', 100)



print (lina.name)
print (goro.name)
print (cowny.__dict__)

print(Hero.__dict__)
print(Hero_Intelligence.__dict__)
