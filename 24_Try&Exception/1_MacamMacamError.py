#error tuh ada dua
#syntax error dan runtime error

#contoh syntax error
# print ('halo dunia)


#contoh runtime error, kalo dimasukin str bakal ValueError
angka = int(input('masukkin angka: '))
print (angka)

#contoh lagi
def pembagian(a,b):
    return a/b

pembilang = int(input('Masukkan pembilang: '))
penyebut = int(input('Masukkan penyebut: '))

print (pembilang,'/',penyebut, '=', pembagian(pembilang,penyebut))
#pembagian dengan 0 juga bisa bikin error




'''NIH MACEM MACEM ERROR NIH (type of exception error)
1. IO Error
2. ImportError
3. ValueError
4. Division by Zero
5. Keyboarad Interuption
6. E0FE Error
'''