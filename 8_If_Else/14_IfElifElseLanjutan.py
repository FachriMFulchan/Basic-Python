#Kombinasi if dengan logika untuk list dan cireng
gorengan = ['bakwan', 'cireng', 'bala-bala', 'gehu', 'combro', 'psiang goreng', 'pukis', 'risoles']
beli = 'gehu'

if beli in gorengan:
    print ('Mamang bilang, " ya, saya jual',beli,'"')

elif not beli in gorengan:
    print ('Mamang bilang, " saya gajual', beli,'"')
print ('\n')


#if buat ngecek adanya string di variable
beli = 'gehu'
karakter = 'a'

if karakter in beli:
    print ('ada', karakter, 'di', beli)

else :
    print ('tidak ada', karakter, 'di', beli)