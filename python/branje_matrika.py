# Ustvarimo prazen seznam vrstic, ki jih bomo prebrali
data = []

# Ukaz 'with' zagotovi, da se datoteka na koncu bloka zapre in nam
# ni potrebno vec paziti na to
with open('../data/matrika.dat', 'r') as f:
    # beremo vrstico po vrstico
    for line in f:
        # odstranimo odvecne presledke
        line = line.strip()
        # locimo podake po presledkih in jih pretvorimo v celo stevilo
        h = [int(x) for x in line.split()]
        # dodamo vrstico
        data.append(h)

print(data)
