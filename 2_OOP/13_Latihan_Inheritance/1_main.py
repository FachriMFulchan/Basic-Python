from Hero import Hero, Hero_intelligence, Hero_strenght

sniper = Hero('sniper')
garo = Hero_intelligence('garo')
lara = Hero_strenght('lara')

sniper.show_info()
garo.show_info()
lara.show_info()

garo.gainExp = 201
lara.gainExp = 201

garo.show_info()
lara.show_info()