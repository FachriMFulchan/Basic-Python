#quiz luar biasa
import numpy as np

a = np.array(([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]))
print (a)

#cara dapet 11,12,16,17
print (a[2:4,0:2])

#cara dapet 2,8,14,20 (pake list)
print (a[[0,1,2,3],[1,2,3,4]])
#satu list nge index barisnya satu lagi kolomnya

#cara dapet 4,5,24,25,29,30
print (a[[0,4,5],3:])


#begitulah caranya nge slice pake list