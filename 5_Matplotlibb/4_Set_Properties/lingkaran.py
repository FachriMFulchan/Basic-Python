import numpy as np
import matplotlib.pyplot as plt

#membuat data
jari2 = 5
titik = np.linspace(0,2*np.pi,100)

x = jari2 * np.cos(titik)
y = jari2 * np.sin(titik)

#membuat plot
dataPlot1 = plt.plot(x,y)

#properties
plt.setp(dataPlot1, color = 'r')

#menampilan plot
plt.show()