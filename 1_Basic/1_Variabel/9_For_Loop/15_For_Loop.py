# List sebagai iterable
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

for g in gorengan:
    print (g)
    print (len(g))
print ('\n')
#print(len(g)) itu menghitung panjang tiap anggota string nya
#bakwan 6, cireng 6, tahu isi 8


# String sebagai iterable
bakwan = 'bakwan'
for i in bakwan:
    print (i)
print ('\n')



#For di dalam for
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

Daftar_belanja = [gorengan, buah, sayur]

for subDaftarBelanja in Daftar_belanja:
    print (subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print (komponen)

        