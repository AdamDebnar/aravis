import calendar
import datetime as dt
import random

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
            knihy[kniha] = int(kapitoly)
# KNIHY_END = 'Knihy načítané.' TODO rozhodnúť sa, či tu takéto riadky budú

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
        DEN_PROMPT = 'Chcete zahrnúť ' + den + '? (A/n)'
        print(DEN_PROMPT)
        zahrnut_rozhodnutie = input(PROMPT)
        zahrnut = DECISION[zahrnut_rozhodnutie.casefold()]
        if zahrnut:
            zahrnute_dni.append(index)

# teraz máme
# 1 knihy (dict)
# 2 datum (dt.date), posun (dt.timedelta)
# 3 s_ukoncenim (bool), datum_koncovy ? (dt.date)
# 4 nahodne (bool)
# 5 niektore_dni (bool), zahrnute_dni ? (list)

# generujeme zoznam párov kniha-kapitola
postupny_zoznam = []
nazvy_knih = knihy.keys()
for x in range(knihy.keys()):
    if nahodne:
        vybrata_kniha = nazvy_knih.pop(random.randrange(len(nazvy_knih)))
    else:
        vybrata_kniha = nazvy_knih.pop(0)
    for cislo in range(1, knihy[vybrata_kniha]+1):
        zoznam.append((vybrata_kniha, cislo))

# generujeme tabuľku
hotova_tabulka = []
while True:
    datum_list = [int(clen) for clen in str(datum).split('-')]
    if not len(zoznam):
        break
    if s_ukoncenim and datum > datum_koncovy:
        break
    if niektore_dni:
        if calendar.weekday(*datum_list) not in zahrnute_dni:
            datum += posun
            continue
    kniha, kapitola = zoznam.pop(0)
    datum_pripraveny = '.'.join(datum_list)
    tabulka.append((datum_pripraveny, kniha, kapitola))
    datum += posun

# exportujeme tabuľku
with open('plan.txt', 'w') as plan_manip:
    for skupina in tabulka:
        print(skupina[0], skupina[1], skupina[2], file=plan_manip)
print('Generovanie úspešné.')
