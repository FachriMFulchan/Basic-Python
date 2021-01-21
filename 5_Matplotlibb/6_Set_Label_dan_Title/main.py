import numpy as np
import matplotlib.pyplot as plt

#membuat data
def sinusGenerator (amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
tAkhir = 4
theta = 0

t,y = sinusGenerator(amplitudo, frekuensi,tAkhir,theta)



#membuat plot
judul = 'Grafik Sinusoida\n'
rumus = r'$\mathcal{Y} = A.sin(2 \pi f t + \theta)$' + '\n'
parameter1 = r'$A = $' + str(amplitudo) + ' cm, '
parameter2 = r'$\mathcal{f} = $' + str(frekuensi) + r' $\mathcal{Hz}$' + ','
parameter3 = r' $\theta = $' + str(theta)


plt.plot(t,y)

plt.title(judul + rumus + parameter1 + parameter2 + parameter3)
plt.xlabel('waktu(detik)')
plt.ylabel('magnitude(cm)')

#menampilkan plot
plt.show()