#maxmin dll
import numpy as np

stats = np.array(([1,2,3],[4,5,6]))
print (stats)

#max
print (np.max(stats))
 #axis 0 = row, jadi cari nilai max di antar baris
 #axis 1 = column, jadi nyari nilai max antar kolom

#min
print (np.min(stats))

#sum, ngejumlahin semuanya, yang ada di matriks, bisa juga cuma kolom dan baris aja(pake axis)
print (np.sum(stats))


