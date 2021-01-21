import numpy as np
import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [1,2,3,4,5]

# plt.plot(x,y)
# plt.show()

#buat lingkaran
pi = np.pi
sudut = np.linspace(0,2*pi,100)
jari2 = 5

x = jari2 * np.cos(sudut)
y = jari2 * np.sin(sudut)

plt.plot(x,y)
plt.show()