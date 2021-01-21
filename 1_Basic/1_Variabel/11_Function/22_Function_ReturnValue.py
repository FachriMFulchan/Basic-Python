#fungsi2 sebelumnya tidak menghasilkan nilai
#coba nih ya kita buktiin

def kuadrat (argumen):
    total = argumen ** 2
    print ('hasil kuadrat dari',argumen, 'adalah', total)

# a = kuadrat(4) #ini kalo dimasukin ke variabel
# print (a) #hasilnya none bahkan problem, tidak ada nilai yang dihasilkan fungsi
print ('\n')




#SOLUSI
def kuadrat1 (argumen):
    total = argumen ** 2
    print ('hasil kuadrat dari',argumen, 'adalah', total) #bahkan ini opsional
    return total

a = kuadrat1(4) #ini bakal ke print
print (a) #ini nilai akhir nya aja yang bakal ke print
print ('\n')





#fungsi dengan return value dan multiple argumen
def tambah (angka1, angka2):
    total = angka1 + angka2
    print (angka1, '+', angka2, '=', total)
    return total

a = tambah(3,4)
print (a)




#bonusss
def kali (angka1, angka2):
    total = angka1 * angka2
    return total
print ('3 * 4 =', kali(3,4)) 
#nah jadi yang muncul nya nilai total aja yang udah di return
#YANG BISA DI RETURN TUH APA AJA, LIST TUPLE DICT GAMASALAH