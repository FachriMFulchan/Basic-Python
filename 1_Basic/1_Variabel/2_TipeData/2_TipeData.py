#Integer
data_integer = 10
print ('data: ',data_integer,', bertipe :',type(data_integer))

#float, data dengan koma(riil)
data_float = 1.5
print ('data: ',data_float,', bertipe :',type(data_float))

#String, kumpulan karakter
data_string = 'ucup'
print ('data: ',data_string,', bertipe :',type(data_string))

#Boolean, Biner True/False
data_bool = True
print ('data: ',data_bool,', bertipe :',type(data_bool))


##Tipe data khusus

#Bilangan Complex
data_complex = complex(5,6)
print ('data: ',data_complex,', bertipe :',type(data_complex))
data_complex2 = 1+2j
print ('data: ',data_complex2,', bertipe :',type(data_complex2))

#Tipe data dari bahasa C
#long,double,char,etc
from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print ('data: ',data_c_double,', bertipe :',type(data_c_double))


