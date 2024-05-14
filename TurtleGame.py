
import random
posizionetarta = 20
posizionelepre = 40
indicetarta = posizionetarta -1
indicelepre = posizionelepre -1
lunghezza_lista = 70
percorso: list[str] = ["_"] * lunghezza_lista

def posizione(indicelepre:int , indicetarta:int, percorso:int ):
    for i in percorso:
        if i == indicelepre:
            percorso.remove("_")
            percorso.append("H")
        elif i == indicetarta:
            percorso.remove("_")
            percorso.append("T")

        print(percorso)

def mossatarta(posizionetarta):
    numero = random.randint(1,10)
    if 1 <= numero <= 5:
        posizionetarta += 3

    elif 6 <= numero <= 7:
        if posizionetarta >= 7:
            posizionetarta -= 6

        else:
            posizionetarta =1 

    elif 8<= numero <= 10:
        posizionetarta +=1


def mossalepre(posizione lepre, indicelepre):
    numero = random.randint(1,10)
    if 1 <= numero <= 2:
        posizionetarta *= 0
    
    elif 3 <= numero <= 4:
        posizionelepre += 9






# https://github.com/FedericoFrancescoFalco/esercizi-2.1.git