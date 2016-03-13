# Ustvarimo prazen seznam vrstic, ki jih bomo prebrali
data = []

# Ukaz 'with' zagotovi, da se datoteka na koncu bloka zapre in nam
# ni potrebno vec paziti na to
with open('../data/stolpec.dat', 'r') as f:
    # preberemo celotno datoteko, locimo vrstice in pretvorimo
    # vrednosti v cela stevila
    data = [int(x) for x in f.read().split()]

print(data)

# Lahko pa beremo tudi vrstico po vrstico in sproti kaj delamo s prebranim
with open('../data/stolpec.dat', 'r') as f:
    for line in f:
        print(int(line))
