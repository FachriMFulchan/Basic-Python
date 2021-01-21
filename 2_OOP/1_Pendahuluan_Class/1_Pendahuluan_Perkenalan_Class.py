class Hero(): #template
    pass

hero1 = Hero() #object/instance (instanciate)
hero2 = Hero()
hero3 = Hero()

hero1.name = 'sniper'
hero1.health = 100

hero2.name = 'sven'
hero2.health = 200

hero3.name = 'ucup'
hero3.health = 1000

print (hero1) #hero1 tuh apa sih
print (hero1.__dict__) #punya apa aja
print (hero1.name)