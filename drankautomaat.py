import random 
from decimal import Decimal

#======================================================
# Dit programma genereert een willekeurige prijs,
# en een som die in de drankautomaat wordt ingeworpen.

# Vervolgens berekenen we het nodige wisselgeld, en
# geven het bedrag in zo weinig mogenlijk munten terug.
#======================================================



# een random float genereren tussen twee waardes, 
# omzetten naar een decimal,
# en tot slot afronden tot 2 getallen na de komma
# nodeloos complex (ノಠ益ಠ)ノ彡┻━┻

prijs = round(Decimal(random.uniform(0.01,5.00)), 2)
betaaldeSom = prijs + round(Decimal(random.uniform(0.01,7.00)), 2)
tebetalen = betaaldeSom - prijs
tussentijdsSaldo = tebetalen


# deze munststukkenDictionary bevat een lijst van paren:
# de waarde van het muntstuk, 
# en hoeveel keer dat munstuk moet worden teruggegeven

# kommagetallen worden als string ingeven en omgezet naar decimal, 
# want floats geven afrondingsproblemen
# nodeloos complex (ノಠ益ಠ)ノ彡┻━┻

munststukkenDictionary = {
    Decimal(2): 0,
    Decimal(1): 0,
    Decimal('0.5'): 0,
    Decimal('0.2'): 0,
    Decimal('0.1'): 0,
    Decimal('0.05'): 0,
    Decimal('0.02'): 0,
    Decimal('0.01'): 0
}

tesktPerMunststuk = "{} stuk(ken) van {} €"

print('========================')
print('prijs: {} €'.format(prijs))
print('betaalde som: {} €'.format(betaaldeSom))
print('wisselgeld: {} €'.format(tebetalen))
print('========================')

# Dit is de logica van de applicatie:
# itereren over de dictionary, dus 2, dan 1, dan 0.5, etc...

for muntWaarde, aantalMunten in munststukkenDictionary.items():

    while tussentijdsSaldo - muntWaarde >= 0:
        
        # 'munststukkenDictionary[muntWaarde]' is wat verwarrend:
        # muntWaarde is de 'key', aantalMunten is de 'value' in de dictionary.
        # wat het doet is in de dictionary zoeken welke 'value'
        # overeenkomt met welke 'key', en daarna de value te verhogen met 1
        # zolang tussentijdsSaldo - muntWaarde >= 0.


        # voorbeeld:

        # we zijn in onze while loop waar muntwaarde '2' is
        # tussentijdsSaldo - muntWaarde >= 0
        # 2.1 euro - 2 euro > 0
        # zoek op key '2' want muntwaarde = '2' 
        # de value is oorspronkelijk geinitialiseerd op 0
        # -> munststukkenDictionary[2] = 0
        # voor key '2' wordt de value 1
        # Dus het aantal munten = aantal munten + 1,
        # daarna het resterend bedrag berekenen

        #Doe daarna hetzelfde voor key 1 euro, key 0.5 euro, key 0.2 euro, etc...
        
        munststukkenDictionary[muntWaarde] = munststukkenDictionary[muntWaarde] + 1
        tussentijdsSaldo = tussentijdsSaldo - muntWaarde

        #Zo bekomen we een dictionary met muntwaardes en aangepast aantal munten
        #voorbeeld:
        #munststukkenDictionary = {
        #     Decimal(2): 1,
        #     Decimal(1): 1,
        #     Decimal('0.5'): 1,
        #     Decimal('0.2'): 0,
        #     Decimal('0.1'): 0,
        #     Decimal('0.05'): 0,
        #     Decimal('0.02'): 0,
        #     Decimal('0.01'): 2
        # }

    
    # print enkel de munten die teruggegeven worden,
    #dus enkel wanneer het aantal munten != 0
    
    if munststukkenDictionary[muntWaarde] != 0:
        print(tesktPerMunststuk.format(munststukkenDictionary[muntWaarde], muntWaarde))
print('========================')