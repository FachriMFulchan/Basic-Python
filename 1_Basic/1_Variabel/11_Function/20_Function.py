#Function tuh program template yang bisa dipakai berulang ulang
# def fungsi ():
#     print ('ini adalah fungsi')
# fungsi()


#Fungsi sederhana, tapi fungsi dalam fungsi
def suaraayam():
    print ('kukuruyuk')
def hargaayam():
    suaraayam()
    print ('Harga ayam per 1 kg adalah Rp. 20000')

hargaayam()



#Fungsi dengan input/parameter
def hargatotalayam(kg):
    harga = 20000
    hargatotal = harga*kg
    print ('Harga',kg, 'kg ayam adalah', hargatotal)

masuk = int(input('Ayam nya mau berapa kilo? '))
hargatotalayam(masuk)
hargatotalayam(5)
hargatotalayam(6)
hargatotalayam(12.5)
#jadi bisa dipanggil terus
