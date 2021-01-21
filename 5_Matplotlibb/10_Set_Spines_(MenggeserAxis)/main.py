import numpy as np
import matplotlib.pyplot as plt

#membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

#membuat plot
plt.plot(sudut,y)
plt.title('Grafik Sinusoida')
plt.text(190,1,'magnituda')
plt.text(360,0.1,'sudut')

plt.yticks([-1,-0.5,0,0.5,1])
plt.xticks([0,90,180,270,360],
            [r'$ 0^o $', r'$ 90^o $', r'$ 180^o $',r'$ 270^o $',r'$ 360^o $']
            )


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('outward', 180))
ax.spines['bottom'].set_position(('data', 0))

#menampilkan plot
plt.show()