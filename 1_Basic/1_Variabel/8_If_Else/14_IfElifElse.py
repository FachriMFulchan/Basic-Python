#if bertahap
nilai1 =80
nilai2 =75

if nilai1 == 80:
    print('nilai anda:',nilai1)
    print('step1')
    if nilai2 == 75:
        print ('nilai anda:',nilai2)
        print ('step2')
print('\n')

#tanda == juga bisa diganti sama is, != bisa dgn is not
nilai = 60
if nilai is 60:
    print('nilai anda: ',nilai)

nilai = 60
if nilai is not 50:
    print('nilai anda: ',nilai)
print('\n')


#indeks nilai IPK
nilai = 75

if 80 <= nilai <= 100:
    print ('nilai anda adalah A')
elif 70 <= nilai <= 80:
    print ('nilai anda adalah B')
elif 60 <= nilai <= 70:
    print ('nilai anda adalah C')
elif 50 <= nilai <= 60:
    print ('nilai anda adalah T, lakukan perbaikan')
else:
    print ('maaf anda tidak lulus mata kuliah ini')


