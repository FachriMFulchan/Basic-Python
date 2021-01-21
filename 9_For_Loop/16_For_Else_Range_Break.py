# #ketika nge print range
# for i in range (10,40,5):
#     print (i)

# print(range (10,40,5))
# #kalo di print gaakan muncul da python versi 3




#program menemukan angka, kalo udah ditemuin angkanya lalu di break
#break itu akan mengeluarkan dari proses looping
for i in range(0,40):
    print (i)

    if i == 50:
        print ('angka ditemukan')
        break
else:
    print ('angka tidak ditemukan')