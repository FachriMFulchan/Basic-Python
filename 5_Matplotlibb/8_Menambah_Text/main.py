#nah ini teks nya bebas ditempatin dimana aja
#kalo title label kan tertentu, ini mah bebas

import numpy as np
import matplotlib.pyplot as plt

#Membuat data
def sinusGenerator (amplitudo, frekuensi, waktu, theta):
    t = np.arange(0,waktu, 0.05)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

#membuat plot
plt.plot(t,y)
plt.text(2,0.5, r'$y = \mathcal{A}.sin(2\pi f t)$')
plt.text(2,0.4, r'$\mathcal{A} = 1 cm, \mathcal{f} = 1 Hz$')


#menampilkan show
plt.show()