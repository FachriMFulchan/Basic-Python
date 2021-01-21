#SCOPE VARIABLE : LOKAL
# namaKucing = 'cassandra'

# def rubahNamaKucing(namaBaru):
#     namaKucing = namaBaru
#     print ('nama kucing yang baru adalah: ',namaKucing)

# rubahNamaKucing('Jonathan')  #karena ini masih variable lokal
# print ('jadinya nama kucing adalah: ', namaKucing)  #nah ini ga berubah^
# #terus gimana biar variable yang dirubah di fungsi, merubah juga yang diluar fungsi
# print ('\n')




#SCOPE VARIABLE : GLOBAL
namaKucing = 'cassandra'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print ('nama kucing yang baru adalah: ',namaKucing)

rubahNamaKucing('Jonathan')
print ('jadinya nama kucing adalah: ', namaKucing)



#tambahan
makananKucing = 'whiskas'

def kasihMakanKucing(nama, makanan):
    global namaKucing, makananKucing
    namaKucing = nama
    makananKucing = makanan

kasihMakanKucing('alex', 'universal')
print ('Si kucing yang bernama',namaKucing, 'makannya', makananKucing)






'''KESIMPULAN
kalo ada perubahan variable di dalam fungsi, opsinya ada 2
1. lokal, berubahnya udh di dalem fungsi aja, ga keluar luar
walaupun nama variable nya sama di dalem dan diluar gaakan pengaruh satu sama lain

2. global, saling pengaruh, perubahan konten di dalem fungsi pengaruh
caranya adalah menambah syntax GLOBAL TERUS TULIS VARIABEL NYA
'''



