#Operasi bitwise/biner
#operasi masing masing bit

a = 9
b = 5

#OR
c = a | b
print ('\n==========OR==========')
print ('nilai : ',a, ',binary :', format(a, '08b'))
print ('nilai : ',b, ',binary :', format(b, '08b'))
print ('-----------------|-------------------')
print ('nilai : ',c, ',binary :', format(c, '08b'))

#AND
c = a & b
print ('\n==========AND==========')
print ('nilai : ',a, ',binary :', format(a, '08b'))
print ('nilai : ',b, ',binary :', format(b, '08b'))
print ('-----------------&-------------------')
print ('nilai : ',c, ',binary :', format(c, '08b'))

#XOR
c = a ^ b
print ('\n==========XOR==========')
print ('nilai : ',a, ',binary :', format(a, '08b'))
print ('nilai : ',b, ',binary :', format(b, '08b'))
print ('-----------------^-------------------')
print ('nilai : ',c, ',binary :', format(c, '08b'))

#Not
c = ~a
print ('\n==========NOT==========')
print ('nilai : ',a, ',binary :', format(a, '08b'))
print ('-----------------~-------------------')
print ('nilai : ',c, ',binary :', format(c, '08b'))
#nah bitwise not ini rada lier, kaya di mirrorin gitu
#misal asalnya 2 jadi -3, asalnya 9 jadi -10

#biar bisa nampilin fungsi not kaya semestinya gimana??
#kita pake XOR
print ('\n')
d = 0b00001001
e = 0b11111111
print ('nilai :',d, 'binary', format(d,'08b'))
print ('nilai :',e, 'binary', format(e,'08b'))
print ('nilai :',d^e, 'binary', format(d^e,'08b'))
#jadi deh


#shifting

#shift left(>>)
c = a >> 2
print ('\n==========>>==========')
print ('nilai : ',a, ',binary :', format(a, '08b'))
print ('----------------->>-------------------')
print ('nilai : ',c, ',binary :', format(c, '08b'))

#shift right(<<)
c = a << 2
print ('\n==========<<==========')
print ('nilai : ',a, ',binary :', format(a, '08b'))
print ('-----------------<<-------------------')
print ('nilai : ',c, ',binary :', format(c, '08b'))

#digeser ke kiri geser ke kanan gitu aja