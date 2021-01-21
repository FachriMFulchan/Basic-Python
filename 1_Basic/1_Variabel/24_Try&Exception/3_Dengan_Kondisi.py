'''nah yang menyebabkan runtime error bisa banyak kan
bisa Valueerror bisa zerodivision
nah ini tuh bisa dijadiin kondisi
ketika valueerror gimana output nya
ketika zero gimana
'''

while True:
    try:
        pembilang = int(input('Masukkan pembilang: '))
        penyebut = int(input('Masukkan penyebut: '))
        hasil = pembilang/penyebut
        break

    except ValueError:
        print ('yang anda masukkan bukan angka\n')

    except ZeroDivisionError :
        print ('tidak boleh dibagi 0\n')


print ('hasil pembagian adalah ', hasil)