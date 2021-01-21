#ternyata array tuh bisa diibaratkan sbg vektor lohh

import numpy as np

#perkalian dot
a = np.array((2, 1))
b = np.array ((1, 3))
c = np.dot(a, b)
print ('hasil perkalian dot dari a dan b :', c)

d = np.array ((1,3,2))
e = np.array ((3,0,2))
f = np.dot(d, e)
print ('hasil perkalian dot dari d dan e :', f)


#perkalian cross
a = np.array((1,2,0))
b = np.array((2,1,0))

c = np.cross(a,b)
print (c)

d = np.cross(b,a)
print (d)