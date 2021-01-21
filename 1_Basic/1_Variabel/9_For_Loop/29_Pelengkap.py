nama_orang = ['Fachri',
              'Opik',
              'Zamzam',
              'Iyaz',
              'Fauzi'
            ]
profesi = ['Tentara',
           'Engineer',
           'Ustad',
           'Gitaris',
           'Teknisi'
           ]

#ENUMERATE, memisahkan indeks dan konten
for i, nama in enumerate(nama_orang):
    print (i, ':', nama)
print ('\n')

#ZIP, menyatukan list dengan list lain
for nama, kerja in zip(nama_orang, profesi):
    print (nama, ':', kerja)
print ('\n')



#SET, biar urut gimana??
pahlawan = {'Ahmad Yani',
            'Jenderal Soedirman',
            'Soekarno',
            'M. Hatta',
            'Ahmada Soebarjo',
            'Sukarni',
            'Imam Bonjol'
            }
for i in pahlawan: #gak ngurut kan abjad nya
    print (i)
print ('\n')

for i in sorted(pahlawan): 
    print (i)
print ('\n')


#DICTIONARY, tips tipse nge iterable dictionary
marga = {'monyet' : 'mamalia',
               'ikan' : 'pisces',
               'siput' : 'invertebrata',
               'ayam' : 'aves',
               'Trex' : 'dinosaurus'
               }

for i in marga.keys(): #ngeprint keys aja
    print (i)
print ('\n')

for i in marga.values(): #ngeprint value aja
    print (i)
print ('\n')

for i,v in marga.items(): #ngeprint semuanya
    print (i, ':', v)
print ('\n')

for i in marga: #bisa juga gini
    print (i , ':', marga[i])
