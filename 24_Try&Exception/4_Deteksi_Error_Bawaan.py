while True:
    try:
        pembilang = int(input('Masukkan pembilang: '))
        penyebut =  int(input('Masukkan penyebut: '))
        hasil = pembilang / penyebut
        break
    except Exception as err:
        print (err, '\n')

print (hasil)