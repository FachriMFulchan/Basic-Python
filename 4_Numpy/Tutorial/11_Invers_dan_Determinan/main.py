import numpy as np

a = np.array(((1,-1), (1,1)))
print ('matriks A : ')
print (a)


#determinan matriks
det_a = np.linalg.det(a)
print ('nilai determinan dari A : ', det_a)


#inverse matriks
inv_a = np.linalg.inv(a)
print ('matriks invers dari A : ')
print (inv_a)

#kalo a dan inversenya dikaliin
print('kalo a dan inversenya dikaliin :')
c = np.dot(a, inv_a)
print (c)


c = np.dot(inv_a, a)
print (c)

'''DENGAN INI KITA BISA MENYELESAIKAN PERSAMAAN LINERA'''