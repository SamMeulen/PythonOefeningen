import random
from locale import format


"""
Dit programma genereert een willekeurige prijs,
en een som die in de drankautomaat wordt ingeworpen.

Vervolgens berekenen we het nodige wisselgeld, en
geven het bedrag in zo weinig mogenlijk munten terug.
"""

prijs = random.randrange(1,500)
betaaldeSom = prijs + random.randrange(1,700)
tebetalen = betaaldeSom - prijs
tussentijdsSaldo = tebetalen

"""
deze dictionary bevat een lijst van paren:
de waarde van het muntstuk, 
en hoeveel keer dat munstuk moet worden teruggegeven
"""
munststukkenDictionary = {
    200: 0,
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

tesktPerMunststuk = "{} stuk(ken) van {} €"

"""
om afrondingsfouten te vermijden, werken we met 
integers die we door 100 delen bij het printen 
van de tekst
"""
print('========================')
print('prijs: {} €'.format(prijs/100))
print('betaalde som: {} €'.format(betaaldeSom/100))
print('wisselgeld: {} €'.format(tebetalen/100))
print('========================')

"""
itereren over de dictionary, dus 200, dan 100, dan 50, etc...
"""
for muntWaarde, aantalMunten in munststukkenDictionary.items():

    while tussentijdsSaldo - muntWaarde >= 0:
        """
        'munststukkenDictionary[muntWaarde]' is wat verwarrend:
        wat het doet is uit de dictionary op de 'pagina' 
        van de muntwaarde de waarde van het aantal munten 
        opzoeken, en daarna te verhogen met 1. 
        Dus het aantal munten = aantal munten + 1,
        daarna het resterend bedrag berekenen
        """
        munststukkenDictionary[muntWaarde] = munststukkenDictionary[muntWaarde] + 1
        tussentijdsSaldo = tussentijdsSaldo - muntWaarde

    """"
    print enkel de munten die teruggegeven worden
    """
    if munststukkenDictionary[muntWaarde] != 0:
        print(tesktPerMunststuk.format(munststukkenDictionary[muntWaarde], muntWaarde/100))
print('========================')