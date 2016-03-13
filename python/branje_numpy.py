# Uvozimo modul `numpy`
import numpy as np
# Uvozimo modul `matplotlib` (za graf)
import matplotlib.pyplot as plt

# Preberemo podatke o vremenu iz datoteke
data = np.loadtxt('../data/TG_STAID003331.txt',  # pot do datoteke
                  skiprows=20,     # izpustimo prvih 20 vrstic
                  delimiter=',',   # podatke locimo po vejici
                  usecols=(1, 2))  # zanimata nas samo drugi in tretji stolpec

# Narisemo le drugi stolpec iz podatkov (torej tretji)
plt.plot(data[:, 1])
plt.show()

# Vec o preprostem risanju grafov v 'matplotlib_1.py'
