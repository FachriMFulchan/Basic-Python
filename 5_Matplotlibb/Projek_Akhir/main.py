import numpy as np
import matplotlib.pyplot as plt

#1. Membuat data
def sinusGenerator(amplitudo, frekuensi,waktu, theta):
    sudut = np.arange(0,360,0.5)
    y =amplitudo * (np.sin(np.deg2rad(sudut) *frekuensi*waktu + np.deg2rad(theta)))
    return sudut,y

sudut1, y1 = sinusGenerator(1,1,1,0)
sudut2, y2 = sinusGenerator(1,1,1,90)



#2. Membuat plot
dataPlot1 = plt.plot(sudut1, y1, label = 'sin(0)')
dataPlot2 = plt.plot(sudut2, y2, label = 'sin(90)')

#setting legenda
plt.legend(loc = 'best')


#setting title
plt.title('Grafik Sinusoida')


#setting rumus
text1 = r'$\mathcal{Y} = A . sin(2 \pi f t + \theta) $' + '\n'
text2 = r'$\mathcal{A} = 1 cm, \mathcal{f} = 1 Hz$'


plt.text(-15,-0.7,(text1+text2))


#setting parameter
plt.text(360, 0.1, 'degree')
plt.text(190, 1, 'magnitude')


#setting ticks
plt.yticks([-1,-0.5,0,0.5,1])
plt.xticks([0,90,180,270,360],
           [r'$0^o$',r'$90^o$',r'$180^o$',r'$270^o$',r'$360^o$']
            )


#setting spines
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data', 180))
ax.spines['bottom'].set_position(('data', 0))



#setting properties
plt.setp(dataPlot1, color = 'g', linewidth = 4)
plt.setp(dataPlot2, color = 'b', linestyle = '--')


#3.Menampilkan plot
plt.show()