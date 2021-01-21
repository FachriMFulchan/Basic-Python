#Stack tuh LIFO, Queue tuh FIFO
tumpukan = [1,2,3,4,5,6]
print ('data sekarang: ', tumpukan)

#memasukkan data baru
tumpukan.append(7)
print ('data yang masuk:', 7)
print ('data sekarang:', tumpukan)

tumpukan.append(8)
print ('data yang masuk:', 8)
print ('data sekarang:', tumpukan)

out = tumpukan.pop()
print ('data keluar: ',out)
print ('data sekarang: ', tumpukan)

'''kalo remove kan spesifik data yang mau diilangin apa
kalo stack sama queue, ga peduli datanya berapa,
yang penting ada di paling belakang atau ada di paling depan
dan datanya tuh gadihapus tapi dikeluarin, BUAT DIPAKE
'''

#Que gaada built in bawaan python nya jadi bentar nanti