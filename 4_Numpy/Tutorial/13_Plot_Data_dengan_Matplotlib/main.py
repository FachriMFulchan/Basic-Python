import numpy as np
import matplotlib.pyplot as plt

#persamaan garis
#y = 2x + 3

x = np.arange(0,11,1)
print (x)
y = 2 * x + 3
print (y)

# plt.plot(x, y)
# plt.show()



#lingkaran
jari = 5

sudut = np.linspace(0,(2*np.pi), 50)


x2 = jari*np.cos(sudut)
y2 = jari*np.sin(sudut)

plt.plot(x2,y2)
plt.show()