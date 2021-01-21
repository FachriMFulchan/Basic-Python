#waktu untuk memproses data tuple dan list
import timeit

data_list = timeit.timeit(stmt="[1,2,3,4,5,6]", number=100000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6)", number=100000)

print ('waktu untuk memproses: ', data_list)
print ('waktu untuk memproses: ', data_tuple)
