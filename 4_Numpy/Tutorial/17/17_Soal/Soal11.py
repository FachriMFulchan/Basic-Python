import numpy as np

P = np.array(([-1,0],[2,-1]))
print ('Matriks P :')
print (P)

e = P
for i in range(2018):
    a = np.dot(e,P)
    e = a

print('Matriks P pangkat 2019 : ')
print (e)
print('jumlah semua unsurnya:',np.sum(e))


