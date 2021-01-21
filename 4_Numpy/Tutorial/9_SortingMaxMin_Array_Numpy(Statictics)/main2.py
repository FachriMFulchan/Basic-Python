#NGURUTIN MATRIKS
import numpy as np

a = np.floor(np.random.randn(3,3) * 10)
print (a)


print ('nilai max dari a = ', np.max(a))
print ('posisi max dari a ada di = ', np.argmax(a))

print ('nilai min dari a = ', np.min(a))
print ('posisi min dari a ada di = ', np.argmin(a))
print ('\n')



#mengurutkan nilai dan posisinya
print ('mengurutkan nilai a : ')
print (np.sort(a)) #ini ngututin per baris
print (np.argsort(a)) 
