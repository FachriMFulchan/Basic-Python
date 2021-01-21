#reshape dan resize kaya gitu
import numpy as np

before = np.array(([1,2,3,4],[5,6,7,8]))
print (before)

after = np.reshape(before,(2,2,2))
print (after)



#stack (menggabungkan matriks)
#vstack
v1 = np.array([[1,2,3,4]])
v2 = np.array([5,6,7,8])
print (np.vstack((v1,v2,v1,v2)))

#horizontal stack juga sama aja