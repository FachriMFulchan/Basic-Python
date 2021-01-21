import numpy as np

a = np.floor(np.random.randn(1,6) * 10)
print (a)
#jadi random nih array nya tiap di play, random dan di bulatkan


#mengetahui nilai max dan min dan posisinya
print ('nilai max dari a = ', np.max(a))
print ('posisi max dari a ada di = ', np.argmax(a))

print ('nilai min dari a = ', np.min(a))
print ('posisi min dari a ada di = ', np.argmin(a))
print ('\n')



#mengurutkan nilai dan posisinya
print ('mengurutkan nilai a : ')
print (np.sort(a))
print (np.argsort(a)) #ini data yang sebelum di sort ya
