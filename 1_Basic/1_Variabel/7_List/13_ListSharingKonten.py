#Merubah Content dari list
Data = [1,4,9,25,36,49,64]
#Awas ni ati ati
print (Data)
a = Data
a[4] = 87
print (a)
#oke normal, tapi ketika nge print data
print (Data)
#loh ko berubah juga, nah disini a sama Data tuh saling sharing content
#kalo a dirubah Data juga ikut ke rubah, terus gimana caranya biar ga gitu


Data = [1,4,9,25,36,49,64]
a = Data[:] #nah ini a tuh cuma copy konten data, ga sharing data lagi
a[4] = 87
print (Data)
print (a)
