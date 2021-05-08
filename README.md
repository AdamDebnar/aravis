# ARAVIS

## GENERÁTOR DENNÉHO PLÁNU ČÍTANIA BIBLIE PO KAPITOLÁCH

### Prehľad

**Aravis** je konzolový program napísaný v Pythone, ktorý vie vygenerovať prehľadnú
tabuľku čítania Biblie rýchlosťou kapitola denne, v zvolených dňoch v týždni.

### O vstupe a výstupe
Vstupný súbor: knihy.txt
program používa aj vstup z klávesnice počas behu programu:
- začiatočný dátum
- zahrnuté dni v týždni
Výstupný súbor: plan.txt

Program vytvorí plán čítania Biblie na základe vstupných údajov 
zo súborov knihy.txt a zaciatok.txt a uloží ho ako tabuľku do súboru plan.txt.
V súbore knihy.txt sa majú nachádzať požadované knihy s príslušným počtom
kapitol, ktoré sa budú čítať po kapitole od začiatku do konca, každý deň okrem
nedele.

### Moje poznámky

Najprv sa spýtaj na dátum začiatku.
Spýtaj sa na dĺžku plánu.
Spýtaj sa, či chce užívateľ čítať knihy v náhodnom poradí - buď všetky knihy zaradom,
alebo prvá kniha a potom náhodne.
Nakoniec sa spýtaj, či nechce užívateľ vynechať niektoré dni v týždni.