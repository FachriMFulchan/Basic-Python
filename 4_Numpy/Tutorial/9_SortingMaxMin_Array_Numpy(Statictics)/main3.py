#NGURUTIN ARRAY MULTITYPE
import numpy as np

dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [
        ('ucup', 170),
        ('otong', 150),
        ('mario', 160)
        ]

a = np.array(data, dtype = dtipe)
print (a)

print (np.sort(a, order = 'nama'))
print (np.sort(a, order = 'tinggi'))
#kerenn abisss