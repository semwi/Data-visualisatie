# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:53:23 2021

@author: semwijnschenk
"""

import matplotlib.pyplot as plt
import numpy as np

x_verplaatsing = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5])

y_meting1 = np.array([1.480, 1.300, 1.117, 0.930, 0.742, 0.550, 0.363, 0.170, 0.024,
            0.202, 0.392, 0.580, 0.773, 0.960, 1.148, 1.333])
y_meting2 = np.array([1.440, 1.264, 1.090, 0.911, 0.730, 0.545, 0.3607, 
                      0.1840, 0.0057, 0.1760, 0.3534, 0.540, 0.721, 0.900, 1.079, 1.255])
dy = [0.08, 0.07, 0.06, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08]

#zorgt ervoor dat [a1, a2, a3] en [b1, b2, b3], [a1, b1, a2, b2, a3, b3] wordt
y_theoretische_waardes = np.ravel((y_meting1,y_meting2),'F')
y_lijsten = y_theoretische_waardes.reshape(([16, 2]))
y_gemiddelde_theoretische_waardes = np.mean(y_lijsten, axis = 1)



plt.xlabel("verplaatsing x (mm), ± 0,005 mm", fontsize=14)
plt.ylabel("Uitgang U (V)", fontsize=14)

plt.errorbar(x_verplaatsing, y_meting1, c='green', yerr=dy, fmt='.g', elinewidth=1, capsize=3, MarkerFaceColor='green', MarkerEdgeColor='green',label='meting 1')
plt.errorbar(x_verplaatsing, y_meting2, c='blue', yerr=dy, fmt='.b', elinewidth=1, capsize=3, MarkerFaceColor='blue', MarkerEdgeColor='blue',marker ="x", label='meting 1')


plt.plot(x_verplaatsing, y_gemiddelde_theoretische_waardes, c='red', label='theorie')
plt.legend()
plt.grid()

plt.savefig('plot4.EPS')

plt.show()

