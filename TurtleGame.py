
#uso un modulo per generare numeri random
import random

#definisco una funzione con tre argomenti: la posizione generale, quella della tararuga, quella della lepre. in un ciclo da 70 istanti in cui il ciclo for ha tre condizioni per risolversi oppure.

def print_race(positions, hare_pos, tortoise_pos):
    for i in range(70):
        if i == hare_pos and i == tortoise_pos:
            print("OUCH!!!", end="")
        elif i == hare_pos:
            print("H", end="")
        elif i == tortoise_pos:
            print("T", end="")
        else:
            print("_", end="")
    print()

#Le funzioni `tortoise_move()` e `hare_move()` determinano quanto la tartaruga e la lepre si spostano durante ogni turno della gara. All'interno di queste funzioni, viene generato un numero casuale tra 1 e 10. Questo numero rappresenta quanto velocemente la tartaruga o la lepre si muoverà.

def tortoise_move():
    move = random.randint(1, 10)
    if move <= 5:
        return 3
    elif 6 <= move <= 7:
        return -6
    else:
        return 1

def hare_move():
    move = random.randint(1, 10)
    if move <= 2:
        return 0
    elif 3 <= move <= 4:
        return 9
    elif 5 <= move <= 6:
        return -12
    elif 7 <= move <= 9:
        return 1
    else:
        return -2

#definisco una posizione iniziale tra la tartaruga e la lepre. utilizzo il ciclo il ciclo while true che prodeguirà finché non  interrotto dall' istruzione `break`. Le posizioni della lepre e della tartaruga vengono aggiornate ad ogni iterazione utilizzando le funzioni `hare_move()` e `tortoise_move()` , generate da un numero casuale. Con relativa verifica che le posizioni non siano mai inferiori a 1.

def race():
    hare_pos = 1
    tortoise_pos = 1
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        hare_pos += hare_move()
        tortoise_pos += tortoise_move()
        
        if hare_pos < 1:
            hare_pos = 1
        if tortoise_pos < 1:
            tortoise_pos = 1
   
    #uso la funzione `print_race` per stampare la visualizzazione della gara. E una serie di verifiche per capire chi stia vincendo.        
                              
        print_race(70, hare_pos, tortoise_pos)
        
        if hare_pos >= 70 and tortoise_pos >= 70:
            print("IT'S A TIE.")
            break
        elif hare_pos >= 70:
            print("HARE WINS || YUCH!!!")
            break
        elif tortoise_pos >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break

race()

#quando una delle condizioni di vittoria viene soddisfatto,il programma termina.