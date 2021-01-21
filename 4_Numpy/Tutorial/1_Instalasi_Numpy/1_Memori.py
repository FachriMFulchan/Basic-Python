import numpy as np

a = np.array((1,2,3,4),dtype='int32')
print (a)

b = np.array(([1.2,2.2,3.2],[22.2,43.2,50.2]))
print (b)

#get dimensional
# print (np.ndim(a))
# print (np.ndim(b))
# print (np.ndim(c))

# #get shape
# print (np.shape(a))
# print (np.shape(b))

#get jenis memory
print (a.dtype) #pake jenis berapa bit

#get size
print (a.itemsize) #sehingga ada berapa bytes

#get total size
print (a.nbytes) #jumlah nya jadi berapa di a tuh(sesuai berapa angkanya)


print (b.dtype)
print (b.itemsize)
print (b.nbytes)
#float lebih gede penyimpanannya