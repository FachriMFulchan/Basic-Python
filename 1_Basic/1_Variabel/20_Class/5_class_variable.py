#variable yang ada self (yg di dalem method ) tuh variable instance
#nah yang ada diluar method tapi ada didalem class adalah variable class



class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama):
        self.nama = input_nama
        mahasiswa.jumlah_mahasiswa += 1



otong = mahasiswa('otong surotong')
ucup = mahasiswa('michael ucup')
zahra = mahasiswa('zahra fauziah')
 
print (zahra.__dict__) #ternyata variabel yang diisi jadi dict loh
print(mahasiswa.jumlah_mahasiswa)


#jadi bisa dipake buat COUNTER