#fungsi dengan argument sederhana
def siswa(nama):
    print ('siswa ini bernama:',nama)
siswa('mario')


#fungsi dengan keyword argument
def guru(nama, pelajaran):
    print ('guru ini bernama:', nama)
    print ('mengajar:',pelajaran)
guru (nama='Popong', pelajaran='Matematika')
guru (pelajaran = 'olahraga', nama = 'Endang') #nah fungsi keyword tuh ini bisa dibalik balk
guru ('Wahyudi', 'Elektronika') #bisa juga gausah pake keyword sih, tapi gabisa dibalik balik
print ('\n')




#fungsi dengan default argument
def penjagaSekolah(nama, shift = 'siang', galak = 'tidak'):
    print ('penjaga sekolah bernama: ', nama)
    print ('shiftnya: ', shift)
    print ('galak? ', galak)
penjagaSekolah('Entep')
penjagaSekolah('Jomin', shift = 'sore', galak = 'banget')
# penjagaSekolah(shift = 'malem', galak = 'dikit') # ini bakal error
# Jadi fungsi dengan argument default OPTIONAL buat diisi
# tapi yang gaada default argument wajib diisi