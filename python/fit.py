import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Definirajmo funkcijo, ki jo fitamo
f = lambda x, A, B: A * np.exp(B * x)

data = np.loadtxt('../data/boltz.dat', skiprows=1, delimiter=',')

# Klicemo curve_fit, kjer je
#  - sigma: seznam napak y koordinate
#  - p0: zacetni priblizki parametrov (kot so v zaporedju v def. funkcije)
popt, cov = opt.curve_fit(
    f, data[:, 0], data[:, 1], sigma=data[:, 3], p0=[1, 1e-10])

# Napake so koreni diagonalnih elementov kovariancne matrike
perr = np.sqrt(np.diag(cov))

print(popt)
print(perr)

plt.errorbar(data[:, 0], data[:, 1], xerr=data[:, 2], yerr=data[:, 3])
plt.plot(data[:, 0], f(data[:, 0], popt[0], popt[1]))

plt.show()
