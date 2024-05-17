nome_variabile: int = 10
nome_variabile: float = 10
nome_variabile: bool = False
nome_variabile: str = "Ciao"

nome_variabile_ int =10

nome_variabile = nome_variabile + 5
nome_variabile += 5.5

variabile_float: float = 0.0

variabile_float = 5.0 + 10.0

variabile_int: int = 0
variabile_int = 10 + 5

print(nome_variabile)


lunghezza_lista: int = 7
punto_di_mezzo: int = 7 // 2

import math
punto_di_mezzo: float = 3.2
print(math.ceil(punto_di_mezzo))

var_1: bool = True
var_2: bool = False


print(var_1 and var_2)
print(var_1 or var_2)
print(not var_1)


if var_1 and var_2:

    print(f"{var_1 and var_2}")

x: int = 1000

if x > 0 and x < 20:

    if lista[i] > lista[i+1]:
        
        temp: int = lista[i]

        lista[i] = lista[i+1]

        lista[i+1] = temp

    elif var_1 and var_2

    else:



for x in range(10):
    print(f"x = {x}")




a: bool = True
a: bool = True


if a and b:

    print(f"sono nel primo if")


elif a or b:

    print(f"sono nel primo elif")

else:

    print(f"Sono nell'else")


    #tre modi di fare la stessa cosa


lista: list =[1, 2, 3, 5]

for numero in lista:
    print(f"xì2: {numero**2}")

    prima stampa 1, poi 4, poi 9, poi 25


nel caso di
for numero in range(len(lista)):
    print(f"x^2: {list[numero]**2}")

 


contatore: int = 0
while contatore < len(lista):

    print(f"x^2: {lista[contatore]**2}")

    contatore +=1



 #2

 def transform(x: int) -> int:
    if x % 2 == 0:
        x /=2
    else:
        x*=3
        x-=1
    return x


#3

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        stipendio = ore_lavorate *  10
        
    elif ore_lavorate > 40:
        ore_extra = ore_lavorate - 40
        stipendio_extra = ore_extra * 15
        stipendio_40 = 40 * 10
        stipendio = stipendio_40 + stipendio_extra
    return stipendio    
