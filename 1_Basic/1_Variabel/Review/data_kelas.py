siswa = ['Ahmad', 'Akhdan']

def show_data():
    if len(siswa) <= 0:
        print ('BELUM ADA DATA')
    else :
        for i in range(len(siswa)):
            print ([i+1], siswa[i])

def insert_data():
    show_data()
    print ('\n')
    print ('Jenis insert yang mau dipilih')
    print ('[1] Menambah dari belakang')
    print ('[2] Menambah sesuai indeks')
    jenis = int(input('>> '))


    if jenis == 1 :
        siswa_baru = input('Masukkan nama: ')
        siswa.append(siswa_baru)
    
    elif jenis == 2:
        i = int(input('Pilih indeks: '))
        siswa_baru = input('Masukkan nama: ')
        siswa.insert(i-1, siswa_baru)

    else :
        print ('INDEKS SALAH')

def edit_data():
    show_data()

    i = int(input('Pilih indeks data yang mau di edit: '))
    
    if len(siswa) < i:
        print ('INDEKS SALAH')
    
    else:
        siswa_baru = str(input('Nama baru: '))
        siswa[i-1] = siswa_baru

def remove_data():
    show_data()
    i = int(input('Pilih indeks data yang mau di hapus: '))

    if len(siswa) < i:
        print ('INDEKS SALAH')
    
    else :
        siswa.remove(siswa[i-1])



def show_menu() :
    print ('============Data Anggota Kelas 1AEB===========')
    print ('[1] Show Data')
    print ('[2] Insert Data')
    print ('[3] Edit Data')
    print ('[4] Remove Data')
    print ('[5] Exit')
    masuk = int(input('PILIH INDEKS > '))

    if masuk == 1 :
        show_data()
    elif masuk == 2 :
        insert_data()
    elif masuk == 3 :
        edit_data()
    elif masuk == 4 :
        remove_data()
    elif masuk == 5 :
        exit()
    else :
        print ('INDEKS SALAH')
    print ('\n')

while __name__ == "__main__":
    show_menu()