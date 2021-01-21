class Hero():

    __privateJumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPrivate, inputProtected):
        self.name = inputName
        self.health = inputHealth

        #variabel instance private, pake underscore2x
        self.__private = inputPrivate

        #variabel instance protected, ini mah bisa diganti dan diprint, sama kaya variabel publik
        self._protected = inputProtected

lina = Hero('lina',100, 'naon wee', 'mens biore')



## manggil dan ngubah variabel private
# print (lina.__dict__)
# lina.__private = 'huya'
# print (lina.__private)
# print (lina.__dict__) #jadi muncul variabel baru



## manggil dan ngubah variabel protected
# print (lina.__dict__)
# print (lina._protected)
# lina._protected = 'garnier'

# print (lina.__dict__)
# print (lina._protected)




## manggil dan ngubah variable private class
# print (Hero.__dict__)
# Hero.__privateJumlah = '20'
# print (Hero.__privateJumlah)
# print (Hero.__dict__)       #jadi variabel baru juga