import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

# tukaj definiramo funkcijo, ki za korak i popravi podatke v grafu


def animate(i):
    line.set_ydata(np.sin(x + i / 10.0) / i)  # update the data
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25)
plt.show()
