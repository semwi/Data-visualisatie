# -*- coding: utf-8 -*-
"""
Een module om de meetdata in op te slaan.

Created on Thu Apr  8 19:22:45 2021

@author: semwijnschenk
"""


import numpy as np
# De stappen voor de verplaatsing van de LVDT in mm.
x_verplaatsing = np.array([41.5, 53.9, 60.6, 79.4, 86.5])
x_2 = np.array([60.4, 69.7, 78.4, 86.9, 92])
# De resultaten van de eerste meting.
y_meting1 = np.array([408, 556, 618.8, 857.85, 894])
# De resultaten van de tweede meting.
y_meting2 = np.array([912.03, 1062, 1205.4, 1333.3, 1413.75])
# De gemiddelde onnauwkeurig van de twee metingen.
dy = [5, 5, 5, 5, 5]
