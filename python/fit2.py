import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

data = np.loadtxt('../data/boltz.dat', skiprows=1, delimiter=',')

popt, cov = np.polyfit(data[:, 0], np.log(data[:, 1]), 1,
                       w=((data[:, 3] / data[:, 1]) ** (-2)), cov=True)
perr = np.sqrt(np.diag(cov))

print(popt)
print(perr)

print(np.exp(popt[1]), perr[1] * np.exp(popt[1]))

plt.errorbar(data[:, 0], np.log(data[:, 1]), xerr=data[
             :, 2], yerr=data[:, 3] / data[:, 1], fmt="o", color="red")
plt.plot(data[:, 0], data[:, 0] * popt[0] + popt[1])

plt.show()
