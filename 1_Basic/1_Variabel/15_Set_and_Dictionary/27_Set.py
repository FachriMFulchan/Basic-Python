'''SET
1. datanya acak (gaada indeks)
2. kalo ada data yang nilainya sama, dianggap satu
'''
#Cara 1 membuat SETS
superhero = {'wiro sableng', 
            'si buta dari goa hantu', 
            'saras 008', 
            'gundala', 
            'gatot kaca'}

superhero.add('mak lampir')
superhero.add ('gundala')
print (superhero)
print (sorted(superhero))
print ('\n')
#kalo mau di sort pake ini tapi cuma alfabet aja, ga ngaruh ke indexsin




#Cara 2 membuat SETS
superhero = set()
superhero.add('wiro sableng')
superhero.add('saras 008')
superhero.add('gundala')
print (superhero)
print ('\n')





#KERENNYA SETS, bisa union, intersection, substract
ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print (ganjil.union(genap), 'union')
print (ganjil.intersection(prima), 'intersection')
print (prima - genap, 'substract')