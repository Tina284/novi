#Primjer: Napišite funkciju pozdrav() koja ne prima nijedan parametar, a kao rezultat ispisuje "Dobar dan!"
"""
def pozdrav():
    print("Dobar dan!")

pozdrav()
"""

#Primjer: Napišite funkciju kvadrat(a) koja prima broj te vraća kvadrat broja.
"""
def kvadrat(a):
    return a*a

print(kvadrat(4))
"""

#Primjer: Napišite funkciju zbrajanje(a,b,c) koja prima tri broja te iz zbraja.
    #Koja je razlika između print i return?
"""
def zbrajanjeR(a,b,c):
    zbroj = a+b+c
    return zbroj
a = zbrajanjeR(4,5,6)
print("Varijabla a u return: ", a) # a = 15

def zbrajanjeP(a,b,c):
    zbroj = a+b+c
    print("U funkciji: ", zbroj)
a = zbrajanjeP(4,5,6)
print("Varijabla a: ", a) # a = None
"""

#Primjer: Napišite funkciju zbrajanje(a,b,c) koja prima tri broja te iz zbraja. 
#Neka je c zadan na 5, u slučaju da se proslijedi manje parametara.
"""
def zbrajanje(a,b,c=5):
    return a+b+c
zbroj = zbrajanje(2,3)
#zbroj = zbrajanje(2,3,20)
print(zbroj)
"""

#Zadatak 1: Napišite funkciju koja vraća najveći od 5 proslijeđenih brojeva.
    #funkcija max(broj1, broj2...)
"""
def najveci(br1, br2, br3, br4, br5):
    return max(br1, br2, br3, br4, br5)

najveciBr = najveci(726, 58, -23, 87439, 2)
print(najveciBr)
"""
#Zadatak 2: Napišite funkciju koja provjerava nalazi li se broj unutar danog raspona.
    #fja(minR, maxR, broj)
    #fja(2, 10, 7) --> unutar raspona; fja(10, 70, 4) --> izvan raspona
"""
def raspon(minR, maxR, broj):
    if minR <= broj <= maxR:
        return("Broj je u rasponu")
    else:
        return("Broj je izvan danog raspona")

minR = 2
maxR = 10
broj = 70
a = raspon(minR, maxR, broj)
"""
#Zadatak 3: Napišite funkciju koja prima listu brojeva, a vraća filtriranu listu koja sadrži samo neparne brojeve.
"""
def neparnaLista(lista):
    nep = []
    for el in lista:
        if el % 2 != 0:
            nep.append(el)
    return nep

neparni = neparnaLista([48485, 432, 321343, 12132, 54353, 8599])
print(neparni)
"""

#Zadatak 4: Napišite funkciju koja prima ime, prezime, godinu rođenja radnika te početnu plaću.
    #Ako plaća nije proslijeđena funkciji neka je zadana plaća (po defaultu) 1000e.
    #Neka funkcija vrati string oblika:
"""Radnik se zove __ i preziva __. Ima __ godina te mu je početna plaća __."""
"""
def radnik(ime, prezime, godRod, pocPlaca = 1000):
    brG = 2023 - godRod
    rez = f"Radnik se zove {ime} i preziva {prezime}. Ima {brG} godina te mu je početna plaća {pocPlaca}"
    return rez

prvi = radnik("Ante", "Antić", 2001, 800)
drugi = radnik("Mate", "Matić", 1990)
print(prvi)
print(drugi)
"""

#Zadatak 5: Napišite funkciju koja prima jedan parametar (string) i vraća broj velikih i malih slova.
"""
def velMal(a):
    brV = 0
    brM = 0
    for znak in a:
        if znak == znak.upper():
            brV += 1
        elif znak == znak.lower():
            brM += 1
    return brV, brM

prebrojavanje = velMal("KoLiko IMA VeliKIH slOVA")
print(prebrojavanje)
print("Velikih slova ima: ", prebrojavanje[0])
print("Malih slova ima: ", prebrojavanje[1])
"""
#Zadatak 6: Napišite funkciju koja prima parametar tipa int i vraća umožak znamenki primljenog broja.
 #223 --> 12
"""
def umnozak(broj):
    umn = 1
    while broj > 0:
        ost = broj % 10 #zadnja znamenka
        umn *= ost
        broj = broj // 10 #cjelobrojno dijeljenje, "odbacuje" zadnju znamenku
    return umn

print(umnozak(223))
"""

#Zadatak 7: Napišite program koji za svaki broj u rasponu od 1 do 20 vraća njegov kvadrat.
    #Ispišite samo kvadrate koji su djeljivi s 4.


#Zadatak 8: Napišite funkciju koja prima listu i mijenja je na način da elementi prve i druge polovice liste mijenjaju mjesta.
    #Npr. dana lista [1,2,3,4,5,6] vraćena lista [4,5,6,1,2,3]


#Zadatak 9: Napišite funkciju koja za danu listu vraća samo elemente duljine veće od 6.

#Zadatak 10: Napišite funkciju koja prima listu brojeva i ključni broj. 
    #Neka funkcija vraća listu nastalu kao rezultat umnoška elemenata proslijeđene liste i ključnog broja.
    #lista = [1,2,3], kBr = 5 --> rez = [5, 10, 15]


#Zadatak 11: Napišite funkciju koja za dane duljine pravokutnika vraća njegov opseg i površinu.
    # opseg = 2*a + 2*b
    # površina = a * b

#Zadatak 12: Softver za prepoznavanje znakova često griješi kada se dokumenti (osobito oni stari napisani pisaćim strojem) digitaliziraju. Vaš zadatak je ispraviti pogreške u digitaliziranom tekstu. Morate riješiti samo sljedeće pogreške:
    #A se pogrešno tumači kao 4
    #S se pogrešno tumači kao 5
    #O se pogrešno tumači kao 0
    #I je pogrešno protumačeno kao 1
#Primjer "4K0" --> "AKO"; "5JED1" --> "SJEDI"


