import math

def keliling_persegi(sisi):
    print ('keliling persegi')
    return sisi + sisi + sisi + sisi

def keliling_persegi_panjang(panjang,lebar):
    print ('keliling persegi panjang')
    return panjang + lebar + panjang + lebar

def keliling_lingkaran(jarijari):
    print ('keliling lingkaran ')
    return 2 * 3.14 * jarijari

def keliling_segitiga_teratur(alas,tinggi):
    print ('keliling segitiga teratur')
    c = math.sqrt(((1/2 * alas)**2) + (tinggi ** 2))
    keliling = c + c + alas
    return keliling

def keliling_segitiga_sikusiku(alas, tinggi):
    print ('keliling segitiga siku-siku')
    c = math.sqrt(((alas)**2) + (tinggi ** 2))
    keliling = c + c + alas
    return keliling