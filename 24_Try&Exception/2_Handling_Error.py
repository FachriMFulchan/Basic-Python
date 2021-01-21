'''nah runtime error tuh bisa bikin program kita tuh keluar
dari loop, nah gimana cara penanganan error tsb
biar mudah gitu, pake try and exception
'''

try:
    5/0
except:
    print('error bruh')

#jadi kaya if else, kalo try nya error masuk ke except
#penerapannya disini nih

while True:
    try:
        angka = int(input('Masukkan angka: '))
        break
    except:
        print ('yang anda masukkan bukan angka')

print('berhasil yang anda masukkan adalah angka:', angka)

'''nah ini tapi cuma bisa ngedeteksi error aja
tanpa tahu error nya apa, kalo tau kondisi errornya apa
setiap jenis error input nya bisa beda loh'''