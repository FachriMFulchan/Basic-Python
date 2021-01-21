#Operasi logika atau boolean
#not, or, and or

#NOT
# print('========NOT======')
# a = False
# c = not a
# print ('data a =',a)
# print ('---------Not')
# print ('data c =', c)
# print ('\n')


#OR
print('========OR======')
a = True
b = True
c = a or b
print (a, ' OR', b,' =',c)
a = True
b = False
c = a or b
print (a, ' OR', b,'=',c)
a = False
b = True
c = a or b
print (a, 'OR', b,' =',c)
a = False
b = False
c = a or b
print (a, 'OR', b,'=',c)
print ('\n')

#And
print('========AND======')
a = True
b = True
c = a and b
print (a, ' and', b,' =',c)
a = True
b = False
c = a and b
print (a, ' and', b,'=',c)
a = False
b = True
c = a and b
print (a, 'and', b,' =',c)
a = False
b = False
c = a and b
print (a, 'and', b,'=',c)
print ('\n')

#XOR (akan true jika salah satu true)
print('========XOR=======')
a = True
b = True
c = a ^ b
print (a, ' XOR', b,' =',c)
a = True
b = False
c = a ^ b
print (a, ' XOR',b,'=',c)
a = False
b = True
c = a ^ b
print (a, 'XOR', b,' =',c)
a = False
b = False
c = a ^ b
print (a, 'XOR', b,'=',c)