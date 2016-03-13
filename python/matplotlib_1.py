import matplotlib.pyplot as plt
import numpy as np

# Naredimo sto tock med 0 in 1
x = np.linspace(0, 1, 100)

# Narisemo tri krivulje na isti graf
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

# Oznacimo osi
plt.xlabel('x label')
plt.ylabel('y label')

# Dolocimo naslov grafa
plt.title("Simple Plot")

# Narisemo legendo
plt.legend()

# Prikazemo graf
plt.show()
