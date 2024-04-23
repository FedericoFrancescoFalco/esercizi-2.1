#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!


#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
# Definisci una lista di animali
animali = ["cane", "gatto", "coniglio"]

# Stampo il nome di ogni animale usando un ciclo for
for animale in animali:
    print(animale)

# Poi, stampo una frase su ciascun animale
for animale in animali:
    print("Un", animale, "sarebbe un ottimo animale domestico.")

# Alla fine, stampo ciò che questi animali hanno in comune
print("Ognuno di questi animali li ho avuti in passato")


#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
# Utilizza un ciclo for per stampare i numeri da 1 a 20
for numero in range(1, 21):
    print(numero)


#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
# Creiamo una lista di numeri da uno a un milione
numeri = list(range(1, 1000001))

# Utilizziamo un ciclo for per stampare i primi dieci numeri
for numero in numeri[:10]:
    print(numero)


#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.
# Creiamo una lista di numeri da uno a un milione
numeri = list(range(1, 1000001))

# Verifico se la lista inizia da uno e finisce a un milione
print("Numero minimo nella lista:", min(numeri))
print("Numero massimo nella lista:", max(numeri))

# Calcolo la somma di tutti i numeri nella lista
somma_totale = sum(numeri)
print("Somma di tutti i numeri da uno a un milione:", somma_totale)

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.
# Creo una lista di numeri dispari da 1 a 20 utilizzando l'argomento di passo della funzione range()

# Creo una lista di numeri dispari da 1 a 20 utilizzando l'argomento di passo della funzione range()
numeri_dispari = list(range(1, 21, 2))

# Eseguo ogni numero con un ciclo for
for numero in numeri_dispari:
    print(numero)


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
# Use a for loop to print the numbers in your list.

# Creo una lista dei multipli di 3, da 3 a 30
multipli_di_3 = [numero for numero in range(3, 31) if numero % 3 == 0]

# Eseguo ogni numero con un ciclo for
for numero in multipli_di_3:
    print(numero)


#4-8. Cubes: A number raised to the third power is called a cube. 
#For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

# Creo una lista dei primi 10 cubi
cubi = [numero ** 3 for numero in range(1, 11)]

# Eseguo ogni cubo con un ciclo for
for cubo in cubi:
    print(cubo)


#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
# Utilizziamo una lista per generare una lista dei primi 10 cubi
cubi = [numero ** 3 for numero in range(1, 11)]

# Eseguiamo la lista dei cubi
print(cubi)


#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

# Creo una lista dei multipli di 3, da 3 a 30
multipli_di_3 = [numero for numero in range(3, 31) if numero % 3 == 0]

# Stampo ogni numero con un ciclo for
for numero in multipli_di_3:
    print(numero)

# Stampo i primi tre elementi della lista
print("I primi tre elementi nella lista sono:", multipli_di_3[:3])

# Stampo tre elementi dal mezzo della lista
lunghezza = len(multipli_di_3)
indice_inizio = lunghezza // 3
indice_fine = indice_inizio + 3
print("Tre elementi dal mezzo della lista sono:", multipli_di_3[indice_inizio:indice_fine])

# Stampo gli ultimi tre elementi della lista
print("Gli ultimi tre elementi nella lista sono:", multipli_di_3[-3:])


#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message My favorite pizzas are:,
# and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:
# and then use a for loop to print the second list. 
#Make sure each new pizza is stored in the appropriate list.

# Lista originale delle pizze
mie_pizze = ["Margherita", "Capricciosa", "Diavola"]

# ottengo una copia della lista
pizze_amico = mie_pizze[:]

# Aggiungo una nuova pizza alla lista originale
mie_pizze.append("Quattro_formaggi")

# Aggiungo una pizza diversa alla lista dell'amico
pizze_amico.append("Marinara")

# Stampo le mie pizze preferite
print("Le mie pizze preferite sono:")
for pizza in mie_pizze:
    print(pizza)

# Stampo le pizze preferite dell'amico
print("\nLe pizze preferite dell'amico sono:")
for pizza in pizze_amico:
    print(pizza)


#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

# Lista delle mie pietanze preferite
miei_piatti = ["pizza", "pasta", "bistecca"]

# Lista delle pietanze preferite dell'amico
piatti_amico = ["hamburger", "patatine fritte", "gelato"]

# Stampo le mie pietanze preferite con un ciclo for
print("Le mie pietanze preferite sono:")
for cibo in miei_piatti:
    print(cibo)

# Stampo le pietanze preferite dell'amico con un ciclo for
print("\nLe pietanze preferite dell'amico sono:")
for cibo in piatti_amico:
    print(cibo)


#4-14. PEP 8: Look through the original PEP 8 style guide at https://peps.python.org/pep-0008/ 
#You won’t use much of it now, but it might be interesting to skim through it.

#4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.