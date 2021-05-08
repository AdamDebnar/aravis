'''

'''

import calendar
import datetime as dt

# SPOLOČNÉ

PROMPT = '> '

# ÚVOD

ZACIATOK = 'Program "aravis" (tvorca plánu čítania Biblie) sa spustil.'

print(ZACIATOK)

# INPUT

KNIHY_SUBOR = 'knihy.txt'
DATUM_PROMPT = 'Zadajte počiatočný dátum plánu.'
knihy = {}

# 1) získame slovník kníh s počtom ich kapitol
with open(KNIHY_SUBOR) as knihy_manip:
    for riadok in knihy_manip:
        if riadok:
            kniha, kapitoly = riadok.rstrip().split()
            knihy[kniha] = kapitoly

# 2) získame dátum začiatku
print(DATUM_PROMPT)
datum = [int(clen) for clen in input(PROMPT).split()]
datum = dt.date(*datum[::-1])
posun = dt.timedelta(days=1)

# generujeme zoznam párov kniha-kapitola
zoznam = []
for cislo_knihy, kniha in enumerate(knihy):
    for cislo in range(1, kapitoly[cislo_knihy]+1):
        zoznam.append((kniha, cislo))

# generujeme tabuľku
tabulka = []
while True:
    if not len(zoznam):
        break
    if calendar.weekday(*[int(clen) for clen in str(datum).split('-')]) != 6:
        # 6 == nedeľa
        kniha, kapitola = zoznam.pop(0)
        tabulka.append((datum, kniha, kapitola))
    datum += posun

# exportujeme tabuľku
with open('plan.txt', 'w') as plan_manip:
    for skupina in tabulka:
        print(skupina[0], skupina[1], skupina[2], file=plan_manip)
print('Generovanie úspešné.')
