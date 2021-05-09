import calendar
import datetime as dt

PROMPT = '> '
DECISION = {'a': True, 'n': False}

# ÚVOD

ZACIATOK = 'Program "aravis" (tvorca plánu čítania Biblie) sa spustil.'
print(ZACIATOK)

# INPUT

# TODO podmienky, výnimky, formáty

# potrebujeme
# slovník kníh a kapitol
# dátum začiatku <
# dĺžku plánu <
# náhodné poradie <
# ktoré dni v týždni <

# možno pridaj "Zaznamenané / Chybný vstup"

# 1) získame slovník kníh s počtom ich kapitol - zo súboru
KNIHY_SUBOR = 'knihy.txt'
KNIHY_OTAZKA = ('Skontrolujte zoznam kníh s kapitolami v súbore ' 
+ KNIHY_SUBOR + ' a ak ste spokojný, stlačte ENTER >> ')
enter = input(KNIHY_OTAZKA)
knihy = {}
with open(KNIHY_SUBOR) as knihy_manip:
    for riadok in knihy_manip:
        if len(riadok) and riadok[0] != '\n':
            kniha, kapitoly = riadok.rstrip().split()
            knihy[kniha] = kapitoly
KNIHY_END = 'Knihy načítané.'

# 2) získame dátum začiatku - od užívateľa
DATUM_PROMPT = 'Zadajte počiatočný dátum plánu.'
datum = posun = None
print(DATUM_PROMPT)
datum = [int(clen) for clen in input(PROMPT).split()]
datum = dt.date(*datum[::-1])
posun = dt.timedelta(days=1)

# 3) získame dĺžku plánu
KONCOVY_DATUM_PROMPT = 'Chcete zadať koncový dátum plánu? (A/n)'
print(KONCOVY_DATUM_PROMPT)
koncovy_datum_rozhodnutie = input(PROMPT)
s_ukoncenim = DECISION[koncovy_datum_rozhodnutie.casefold()]
datum_koncovy = None
if s_ukoncenim:
    KONCOVY_DATUM_PROMPT_2 = 'Zadajte koncový dátum plánu.'
    print(KONCOVY_DATUM_PROMPT_2)
    datum_koncovy = input(PROMPT)
    datum_koncovy = dt.date(*datum[::-1])  # TODO reversed() ? .->.

# 4) opýtame sa na náhodné poradie
PORADIE = 'Chcete knihy usporiadať náhodne? (A/n)'
print(PORADIE)
nahodne_rozhodnutie = input(PROMPT)
nahodne = DECISION[nahodne_rozhodnutie.casefold()]

# 5) dni v týždni
TYZDEN = 'Chcete vybrať konkrétne dni v týždni pre čítanie plánu? (A/n)'
print(TYZDEN)
tyzden_rozhodnutie = input(PROMPT)
niektore_dni = DECISION[tyzden_rozhodnutie.casefold()]
if niektore_dni:
    DNI_PROMPT_BEGIN = 'Postupne budete vyberať, či bude ten-ktorý deň v týždni zahrnutý.'
    dni_kluce = ('pondelok', 'utorok', 'streda', 'štvrtok', 'piatok', 'sobota', 'nedeľa')
    zahrnute_dni = []
    for index, den in enumerate(dni_kluce):
        # input
        zahrnut = None  # TODO remake
        if zahrnut:
            zahrnute_dni.append(index)

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
