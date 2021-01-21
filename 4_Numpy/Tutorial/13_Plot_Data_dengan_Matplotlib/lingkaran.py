import numpy as np
import matplotlib.pyplot as plt

''' lingkaran gausah pake rumus x2 + y2 = r2 RIBETT
pake ini aja lebih gampang
tentuin titik titiknya dari 0 - 2phi
x = jari2 * cos(titik)
y = jari2 * sin(titik)
'''

jari2 = 5
titik = np.linspace(0, 2*np.pi, 100)

x = jari2 * np.cos(titik)
y = jari2 * np.sin(titik)

plt.plot(x,y)
plt.show()