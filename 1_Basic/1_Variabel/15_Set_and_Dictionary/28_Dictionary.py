#dictionary, ada key sama value

member = {'ID':'219341029',
          'Nama':'Fachri Fulchan',
          'Pekerjaan':'Mahasiswa',
          'Status':'Jomblo',
          }
print (member['Nama'])
print (member.keys()) #ngeprint keys nya aja
print (member.values()) #ngeprint value nya aja
print (member.items()) #ngeprint semuanya,bisa sih member doang
print ('\n')


member1 = {'ID':101,
          'Nama':'Fachri Fulchan',
          'Pekerjaan':'Mahasiswa',
          'Status':'Gold',
        }

member2 = {'ID':102,
           'Nama':'Ujang',
           'Pekerjaan' : 'Teknisi',
           'Status' : 'Diamond'
        }

memberlist = {101:member1, 102:member2}
print (memberlist[101]) 
#dict nya bisa dipanggil lagi nih pake dict


