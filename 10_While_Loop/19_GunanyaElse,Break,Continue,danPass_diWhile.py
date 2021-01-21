#Gunanya else, Break, Continue dan Pass di While

#While dan Else
angka = 0
while angka < 5:
    print ('nilai angka adalah', angka)
    angka += 1
else:
    print ('nilai terakhir dari angka adalah', angka)
# print ('\n')


#While, Else ditambah break
angka = 0
while angka < 10:
    if angka == 5:
        break
    print ('nilai angka adalah', angka)
    angka += 1

else:
    print ('nilai terakhir dari angka adalah', angka)

print ('Terakhir')
#kalo udh break, else nya juga gakebaca, kenapa??
#karena while sama else dalam kasus ini satu sistem 
#dan break itu sebenernya keluar dari sistem



#While dan Continue
angka = 0
while angka < 10:
    if angka == 5:
        print ('cek') #cek nih
        continue
    print ('Nilai angka adalah', angka)
    angka += 1

else:
    print ('nilai terakhir dari angka adalah', angka)
#nah kalo gini bakal infinite loop di angka = 4
#terus gimana??? nih trik nya

angka = 0
while angka < 10:
    if angka == 5:
        angka += 1
        continue
    print ('Nilai angka adalah', angka)
    angka += 1

else:
    print ('nilai terakhir dari angka adalah', angka)