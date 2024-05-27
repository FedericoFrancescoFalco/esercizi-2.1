
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

def tortoise_move(weather,energy):
    move = random.randint(1, 10)
    if weather == "Pioggia":
        move -= 1
    if move <= 5:
        if energy >= 5:
            energy -= 5
            return 3, energy
        else:
            energy += 10
            return 0, energy
    elif 6 <= move <= 7:
        if energy >= 10:
            energy -= 10
            return -6, energy
        else:
            energy += 10
            return 0, energy
    else:
        if energy >= 3:
            energy -= 3
            return 1, energy
        else:
            energy *= 10
            return 0, energy

def hare_move(weather, energy):
    move = random.randint(1, 10)
    if weather == "Pioggia":
        move -= 2
    if move <= 2:
        energy = min(100, energy + 10)
        return 0, energy
    elif 3 <= move <= 4:
        if energy >= 15:
            energy -= 15
            return 9, energy
        else:
            energy *= 10
            return 0, energy

    elif 5 <= move <= 6:
        if energy >= 20:
            energy -= 20
            return 12, energy
        else:
            energy *= 10
            return 0, energy

    elif 7 <= move <= 9:
        if energy >= 5:
            energy -= 5
            return 1, energy
        else:
            energy *= 10
            return 0, energy

    else:
        if energy >= 8:
            energy -= 8
            return 2, energy
        else:
            energy *= 10
            return 0, energy


def change_weather(tick):

    if tick % 10 == 0:
        return random.choice(["Pioggia", "Soleggiato"])
    else:
        return None

def apply_obstacles(position, obstacles):
    if position in obstacles:
        return position + obstacles[position]
    return position

print("BANG !!!!! AND THEY'RE OFF !!!!!")

hare_pos = 0
tortoise_pos = 0
hare_energy = 100
tortoise_energy = 100

tick = 0
weather = "Soleggiato"

obstacles = {15: -3, 30: -5, 45: -7}
bounces = {10: 5, 25: 3, 50: 10}



while True:
    tick += 1
    weather = change_weather(tick) or weather


    hare_move_result, hare_energy = hare_move(weather,hare_energy)
    hare_pos += hare_move_result
    if hare_pos < 0:
        hare_pos = 0
    hare_pos = apply_obstacles(hare_pos, obstacles)
    hare_pos = apply_obstacles(hare_pos, bounces)    

    tortoise_move_result, tortoise_energy = tortoise_move(weather, tortoise_energy)
    tortoise_pos += tortoise_move_result
    if tortoise_pos < 0:
        tortoise_pos = 0
    tortoise_pos = apply_obstacles(tortoise_pos, obstacles)
    tortoise_pos = apply_obstacles(tortoise_pos, bounces)


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


#quando una delle condizioni di vittoria viene soddisfatto,il programma termina.