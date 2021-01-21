#berapa banyak memori yang dimakan tuple dan list
import sys

data_list = [1,2,3,4,5,6,7,8,9,10,'pisang goreng', 'syahrini', 'via vallen']
data_tuple = (1,2,3,4,5,6,7,8,9,10,'pisang goreng', 'syahrini', 'via vallen')

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print (besar_datalist)
print (besar_datatuple)