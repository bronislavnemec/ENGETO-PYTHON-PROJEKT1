'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#Pozn:

# #vsechna mala
# [text1_unified for slovo in text1_unified if slovo.islower()]
# #vsechna velka
# [text1_unified for slovo in text1_unified if slovo.isupper()]
# #kombinace
# [text1_unified for slovo in text1_unified if not text1_unified.islower() and not text1_unified.isupper()]


users = {'bob': '123','ann': 'pass123','mike': 'password123','liz': 'pass123'}

#funkce kontrola pocatecniho pismena
def get_start_upper_state(_):
    return _[0].isupper()

#funkce kontrola celkove velikosti
def get_all_upper_state(_):
    if _.islower() == True:
        return "LOWER"
    elif _.isupper() == True:
        return "UPPER"
    elif _.isupper() == False and slovo.islower() == False:
        return "COMBINED"

#definice promennych
slovo_capital = int()
slova_velkyma = int()
slova_malyma = int()
slova_zacatek_velkym = int()
slova_kombinovana = int()
slova_cisla = int()
list_delek = []
text_unified = []
mnozina_delek = set()
pocet_slov_dane_delky = int(0)
suma_cisel = int()
fail_number = 0
cislo_textu = int()
oddelovac1 = '*'
oddelovac2 = '----------------------------------------'

str_username = input("Zadej prihlasovaci jmeno:")                               #Prihlasovaci sekvence
if str_username in list(users.keys()):
    print(f"Vitej uzivateli: {str_username}")
else:
    print(f"Nespravne uzivatelske jmeno:")
    exit()

while fail_number < 3:                                                          #povoli 3 chyby pri zadani hesla
    str_password = input("Zadej heslo:")
    if str_password not in list(users.values()):
        fail_number += 1
        if fail_number < 3:
            print(f"Zadal jsi nesprávné heslo!")
            continue
        print(f"Zadal jsi 3x spatne zprihalsovaci udaje - to je tvuj konec!!!!")
        exit()
    else:
        print(f"Prihlasovaci udaje jsou OK, muzeme pokracovat.")
        break

print(oddelovac2)                                                               #Zacatek dialogu
print(f"Welcome to the app, {str_username}")
print(f"We have 3 texts to be analyzed.")
print(oddelovac2)

try:
    cislo_textu = int(input("Vloz cele cislo mezi 1 a 3:")) - 1                 #posunuti indexu v TEXTS
    if cislo_textu not in range(3):
        print("Nebyla vybrana povolena hodnota, konec programu!")
        exit()
except:
    print("Nebyla vybrana povolena hodnota, konec programu!")
    exit()

print(oddelovac2)
text = TEXTS[int(cislo_textu)].split()                                           #vyber zadaneho textu
nove_slovo = []
#unifikace textu - odstraneni nezadoucich znaku
for slovo in (text):
    text_unified.append(slovo.strip(",.:;+-*+ˇ"))

#vyhodnoceni velikosti pismen a soucet cisel

for upr_slovo in (text_unified):
    if upr_slovo.isnumeric():                                       #vyhleda a zpracuje cisla
#        print(f"Pozor***************:), {upr_slovo} je cislo")
        slova_cisla += 1
        suma_cisel += int(upr_slovo)
        continue

    delka_slova = len(upr_slovo)                                    #zpracuje delku slov, vola preddefinovane funkce
    list_delek.append(delka_slova)                                  #vytvori seznam delek slov

    velikost = get_all_upper_state(upr_slovo)
    if get_start_upper_state(upr_slovo) == True:                    #Zacina slovo na velke pismeno?
        slova_zacatek_velkym += 1
#        print(f"Slovo {upr_slovo} je kapitalni.")
        if velikost == "UPPER":
            slova_velkyma += 1
#            print(f"Slovo {upr_slovo} je VELKYMA.")
#        else:
#            slova_kombinovana += 1
#            print(f"Slovo {upr_slovo} je kombinovane.")

    else:
#        print(f"Slovo {upr_slovo} neni kapitalni.")
        if velikost == "LOWER":
            slova_malyma += 1
#            print(f"Slovo {upr_slovo} je malyma.")

print(f"There are {suma_cisel} words in the selected text.")            #Tisk vysledku
print(f"There are {slova_zacatek_velkym} titlecase words.")
print(f"There are {slova_velkyma} uppercase words.")
print(f"There are {slova_malyma} lowercase words.")
print(f"There are {slova_cisla} numeric strings.")
print(f"The sum of all the numbers is {suma_cisel}.")

mnozina_delek = set(list_delek)

print(oddelovac2, "LEN|    OCCURENCES    |NR".center(len(oddelovac2)), oddelovac2, sep='\n')

for i in (mnozina_delek):
    pocet = list_delek.count(i)
#    print(f"pocet slov dlouhych: {i} v textu je  {pocet}.")
    print(f"""{i:>10}|{pocet*oddelovac1: <18}|{pocet}""")

print(oddelovac2)