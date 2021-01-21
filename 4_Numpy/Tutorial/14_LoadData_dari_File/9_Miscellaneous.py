#Load Data From File
import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',',dtype=int)
#bisa juga pake filedata.astype('int32')
print (filedata)


# #boolean masking and advanced indexing
# print (filedata > 50)
# print (filedata[filedata > 50]) #pilih data yang lebih dari 50 aja

# #you can index with list in numpy, makanya yang diatas bisa dilakuin
# a = np.array([1,2,3,4,5,6,7,8,9])
# print (a[[0,1,2]])


c = (filedata >50) & (filedata < 100)
print (c)