import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Nastavitve zapisovanja animacije v datoteko (v tem primeru video)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=25,  # slicice na sekundo - hitrost videa
                bitrate=3600)  # kvaliteta videa

fig = plt.figure()
x = np.arange(-9, 10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)

# Tukaj generiramo posamezne slike in jih potem animiramo
ims = []
for add in np.arange(15):
    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

im_ani = animation.ArtistAnimation(fig,  # figure, ki ga animiramo
                                   ims,  # generirane slike
                                   # interval menjave slike (samo za predogled)
                                   interval=50,
                                   repeat_delay=3000,  # cas ponovitve predogleda
                                   blit=False)

im_ani.save('animacija.mp4',  # ime datoteke
            writer=writer,  # povemo, kako zapisat
            dpi=200)  # resolucija = velikost * dpi
