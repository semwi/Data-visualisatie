# -*- coding: utf-8 -*-
"""
Een module die data visualiseert.

Created on Wed Mar 31 09:53:23 2021

@author: semwijnschenk
"""

import matplotlib.pyplot as plt
import numpy as np
import data

plt.plot(data.x_verplaatsing, data.y_meting1, c="green")
plt.plot(data.x_2, data.y_meting2, c="blue")
plt.plot(0,0)
class maak_grafiek():
    """Een klasse die een grafiek maakt."""

    def __init__(self):
        """Initialiseer de grafiek."""
        # Voeg de 'error bars' toe aan de grafiek.
        self.grafiek_meetonnauwkeurigheid()
        # Voeg assentitels toe aan de grafiek.
        self.grafiek_as_titels()
        # Visualiseer de grafiek
        self.visualiseer_grafiek()

    #def trendlijn(self):
        """Een functie die een trendlijn, gemiddeld uit de twee data sets,
        voor de grafiek maakt."""
        # Ravel zorgt ervoor dat de arrays [a1, a2, a3] en
        # [b1, b2, b3], de array [a1, b1, a2, b2, a3, b3] wordt.
        y_theoretische_waardes = np.ravel(
            (data.y_meting1, data.y_meting2), 'F')

        # Reshape verandert de array [a1, b1, a2, b2, a3, b3] naar [a1, b1],
        # [a2, b2] en [a3, b3]
        y_lijsten = y_theoretische_waardes.reshape(([16, 2]))

        # Mean neemt het gemiddelde van elke array en verander deze terug naar
        # 1 array. Dus: [a1, b1], [a2, b2] en [a3, b3] wordt [((a1+b1)/2),
        # ((a2+b2)/2), ((a3+b3)/2)]
        y_gemiddelde_theoretische_waardes = np.mean(y_lijsten, axis=1)

        # Plot de trendlijn in de grafiek,
        # maak deze rood en voeg deze toe in de legenda.
        plt.plot(data.x_verplaatsing, y_gemiddelde_theoretische_waardes,
                 c='red', label='trendlijn')

    def grafiek_meetonnauwkeurigheid(self):
        """Een funtie die meetonnauwkeurigheids
        punten toevoegd aan de grafiek"""
        # Voeg voor meting 1 meetonnauwkeurigheid punten toe, maak deze groen,
        # met als marker een bolletje en voeg deze toe aan meting 1.
        plt.errorbar(data.x_verplaatsing, data.y_meting1, c='green',
                     yerr=data.dy, fmt='.g', elinewidth=1, capsize=3,
                     MarkerFaceColor='green', MarkerEdgeColor='green',
                     label='lens 1')

        # Voeg voor meting 2 meetonnauwkeurigheid punten toe, maak deze blauw,
        # met als marker een kruisje en voeg deze toe aan meting 1.
        plt.errorbar(data.x_2, data.y_meting2, c='blue',
                     yerr=data.dy, fmt='.b', elinewidth=1, capsize=3,
                     MarkerFaceColor='blue', MarkerEdgeColor='blue',
                     marker="x", label='lens 2')

    def grafiek_as_titels(self):
        """Een funtie die assen titels toe voegt aan de grafiek"""
        # Voeg op de x-as een titel toe en maak de lettergrote 14.
        plt.xlabel("d0 + di", fontsize=14)

        # Voeg op de y-as een titel toe en maak de lettergrote 14.
        plt.ylabel("d0 * di", fontsize=14)

    def visualiseer_grafiek(self):
        """Een funtie die de grafiek visualiseert en de grafiek opslaat
        als EPS bestand."""
        # Maak de lagenda.
        plt.legend()
        # Maak de ruitjes.
        plt.grid()
        # Sla de grafiek op als svg bestand.
        plt.savefig('Data en visualisatie.svg')
        # Laat de plot zien.
        plt.show()
        

        
maak_grafiek()
