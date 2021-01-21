#Latihan konversi satuan temperatur

#Program konversi Celcius ke satuan lain
print ('\nPROGRAM KONVERSI TEMPERATUR \n')

def Kcelcius():
    celcius = float(input('Masukkan suhu dalam Celcius :'))
    print ('suhu adalah', celcius, 'Celcius')

    #Reamur
    reamur = (4/5)*celcius
    print ('suhu dalam reamur adalah', reamur, 'Reamur')

    #Fahrenheit
    fahrenheit = ((9/5)*celcius) + 32
    print ('suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')

    #Kelvin
    kelvin = celcius + 273
    print ('suhu dalam kelvin adalah', kelvin, 'Kelvin')


def Kreamur():
    #Program konversi Reamur ke satuan lain
    reamur = float(input('Masukkan suhu dalam Reamur :'))
    print ('suhu adalah', reamur, 'Reamur')

    #celcius
    celcius = (5/4)*reamur
    print ('suhu dalam celcius adalah', celcius, 'Celcius')

    #fahrenheit˚
    fahrenheit = ((9/4)*reamur)+32
    print ('suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')

    #kelvin
    kelvin = ((5/4)*reamur)+273
    print ('suhu dalam kelvin adalah', kelvin, 'Kelvin')


def Kfahrenheit():
    #Program konversi Fahrenheit ke satuan lain
    fahrenheit = float(input('Masukkan suhu dalam fahrenheit: '))
    print ('suhu adalah', fahrenheit, 'Fahrenheit')

    celcius =  (5/9)*(fahrenheit-32)
    print ('suhu dalam celcius adalah', celcius, 'Celcius')

    reamur = (4/9)*(fahrenheit-32)
    print ('suhu dalam reamur adalah', reamur, 'Reamur')

    kelvin  = ((5/9)*(fahrenheit-32))+273
    print ('suhu dalam kelvin adalah', kelvin, 'Kelvin')

def Kkelvin():
    #Program konversi Kelvin ke satuan lain
    kelvin = float(input('Masukkan suhu dalam kelvin: '))
    print ('suhu adalah', kelvin, 'Kelvin')
    
    celcius = kelvin - 273
    print ('suhu dalam celcius adalah', celcius, 'Celcius')
    
    reamur = (4/5)*(kelvin - 273)
    print ('suhu dalam reamur adalah', reamur, 'Reamur')
    
    fahrenheit = ((9/5)*(kelvin - 273))+32
    print ('suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')
    





def show_menu():
    print ('[1] Konversi Celcius')
    print ('[2] Konversi Reamur')
    print ('[3] Konversi Fahrenheit')
    print ('[4] Konversi Kelvin')
    print ('[5] Exit')
    indeks = int(input('Pilih menu> '))

    if indeks == 1:
        Kcelcius()
    elif indeks == 2:
        Kreamur()
    elif indeks == 3:
        Kfahrenheit()
    elif indeks == 4:
        Kkelvin()
    elif indeks == 5:
        exit()
    
    print ('\n')

while True:
    show_menu()
    










