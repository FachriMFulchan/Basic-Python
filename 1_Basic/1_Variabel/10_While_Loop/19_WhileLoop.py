#Common While
angka = 0
while angka < 5:
    print ('nilai angka adalah',angka)
    angka += 1
print ('di luar while')


#Kondisinya bisa juga pake Boolean
start = True
angka = 0

while start == True:
    print ('di dalam while')
    if angka == 20:
        start = False
        print ('udeh 20')
    angka += 1


