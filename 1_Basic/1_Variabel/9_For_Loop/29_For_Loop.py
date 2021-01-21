#teknik looping pake for kreatif
nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Diaglog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena',
             'Syahrini'
            ]
kumpulan_lagu = ['Akad',
        'Zona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro',
        'Jodohku'
        ]


#cara 1 normal, tapi enggak efektif
i = 0
for band in nama_band:
    print (i, ':', band)
    i += 1
print ('\n')


#cara 2
for indeks in range(len(nama_band)):
    print (indeks, ':', nama_band[indeks])
print ('\n')



#cara 3 pake enumerate
for i, band in enumerate(nama_band):
    print (i, ':', band)
print ('\n')



#KALO MAU MASANG MASANGIN SATU LIST DENGAN LIST YG LAIN, pake ZIP
for band, lagu in zip(nama_band,kumpulan_lagu):
    print (band, ':', lagu)
print ('\n')




#kalo mau nge iterable SET
playlist = {'jaran goyang', 
            'jaran goyang', 
            'ada apa dengan cinta',
            'naluri lelaki',
            'kucing garong',
            'anjing menciap'
            'godzilla'
            }

for i in sorted(playlist): #kendala nya tuh ga berurutan, biar berurutan gimana?
    print (i)
print ('\n')




#kalo mau nge iterable DICTIONARY
playlist2 = {'Payung Teduh' : 'Akad',
             'Fourtwnty' : 'Zona Nyaman',
             'Dialog Dini Hari' : 'Rumahku',
             'Mr. Sonjaya' : 'Sang Filsuf',
             'Parahyena' : 'Sindoro',
            }

for i in playlist2.keys():
    print (i, ':',playlist2[i])
print ('\n')

for i,v in playlist2.items():  #atau juga caranya bisa gini
    print (i,':',v)
