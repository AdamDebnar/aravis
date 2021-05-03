'''
ARAVIS
GENERÁTOR PLÁNU ČÍTANIA BIBLIE PO KAPITOLÁCH

Program vytvorí plán čítania Biblie na základe vstupných údajov 
zo súborov knihy.txt a zaciatok.txt a uloží ho ako tabuľku do súboru plan.txt.
V súbore knihy.txt sa majú nachádzať požadované knihy s príslušným počtom
kapitol, ktoré sa budú čítať po kapitole od začiatku do konca, každý deň okrem
nedele.

Dôležité poznámky
Dátum začiatku sa zadáva v tvare deň [medzera] mesiac_číslom [medzera] rok.
Vstupné súbory musia aj po úprave končiť prázdnym riadkom.
'''

import calendar
import datetime as dt

# získame dáta pre pravý stĺpec
knihy, kapitoly = [], []
with open('knihy.txt') as knihy_subor:
    for riadok in knihy_subor:
        if riadok:
            kniha, kapitola = riadok.rstrip().split()
            knihy.append(kniha)
            kapitoly.append(int(kapitola))

# získame začiatočný dátum
with open('zaciatok.txt') as zaciatok_subor:
    datum = [int(clen) for clen in zaciatok_subor.read().split()]
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
with open('plan.txt', 'w') as plan_subor:
    for skupina in tabulka:
        print(skupina[0], skupina[1], skupina[2], file=plan_subor)
print('Generovanie úspešné.')
