



#Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.


usernames = ["admin" ,"tizio", "caio", "sempronio" ,"pippo" ]
for username in usernames:
	if username == "admin":
		print : "Ciao admin! Vuoi vedere un report completo?"
	else:
		print (f"Ciao {username} benvenuto a bordo!")
		
		
#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.

usernames = [ ]
if usernames:
    for username in usernames:
        print(" Ciao {username}, grazie per esserti loggato oggi!")
else:
    print("Accidenti, ci servono più utenti!")
    
 #5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ["John", "Flea", "Chad", "Anhony", "Josh"]
new_users = ["Arik", "Dave", "George","John","Flea"]
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print( "Ci dispiace, il nickname è già stato scelto!")
	else:
		print(f"The username '{new_user}' is available.")

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.	

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ordinal = "1st"
    elif number == 2:
        ordinal = "2nd"
    elif number == 3:
        ordinal = "3rd"
    else:
        ordinal = str(number) + "th"
    
    print(ordinal)	
    
 
 
 
 
# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
    
    def riepilogo(x):
    	return "in questa lezione spero di aver imparato l'uso della funzione, il problen solving e i valori di ritorno"

riassunto =  riepilogo (1)
print(riassunto)

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.


def Libro_preferito(titolo):
    print(f"Uno dei miei libri preferiti è {titolo}")

Libro_preferito("Alice")

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def maglietta(taglia):
    def scritta(logo):
        print(f"porto una {taglia} e sopra c'è scritto {logo}")
    
    scritta("Nike")

maglietta("XL")

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message

def magliettaa(taglia="L", messaggio="Amo Python"):
    print(f"Creazione di una maglietta di taglia {taglia} con il messaggio: {messaggio}")

# Creo una maglietta L con il messaggio predefinito
magliettaa()

# ne creo anche una media con il messaggio predefinito
maglietta(taglia="m")

# Creo una maglietta qualsiasi con un messaggio personalizzato
magliettaa(taglia="s", messaggio="non mi funziona github da casa")

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default 

def descrivi_citta(nome_citta, paese="Italia"):
    print(f"{nome_citta} si trova in {paese}")


descrivi_citta("Roma")
descrivi_citta("Parigi", "Francia")
descrivi_citta("Stoccarda", "Germania")

#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(nome_citta, paese):
    return f"{nome_citta}, {paese}"

# richiamo la funzione usando tre coppie nazione per poi stampare i valori:
citta1 = city_country("Roma", "Italia")
print(citta1)

citta2 = city_country("Parigi", "Francia")
print(citta2)

citta3 = city_country("Stoccarda", "Germania")
print(citta3)

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album

def make_album(nome_artista, titolo_album, numero_brani=None):
    album = {
        "artista": nome_artista,
        "titolo": titolo_album
    }
    if numero_brani:
        album["numero_brani"] = numero_brani
    return album

# Creo tre dizionari rappresentanti album diversi
album1 = make_album("Red Hot Chili Peppers", "Californication", 15)
print(album1)

album2 = make_album("Metallica", "Black Album", 12)
print(album2)

album3 = make_album("Faith No More", "Angel Dust", 13)
print(album3)


#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.


def make_album(nome_artista, titolo_album, numero_brani=None):
    album = {
        "artista": nome_artista,
        "titolo": titolo_album
    }
    if numero_brani:
        album["numero_brani"] = str(numero_brani)  
    return album

while True:
    nome_artista = input("Inserisci il nome dell'artista dell'album (o 'quit' per uscire): ")
    if nome_artista.lower() == 'quit':
        break
    
    titolo_album = input("Inserisci il titolo dell'album: ")
    
    album = make_album(nome_artista, titolo_album)
    print("Ecco le informazioni sull'album:")
    print(album)
    
 #8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
 
def show_messages(messages):
    
    for message in messages:
        print(message)

messages = ["Ciao!", "Come va?", "Sto bene, grazie!", "Tu?"]
show_messages(messages)
 
 
#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

def send_messages(messages, sent_messages):
   
    for message in messages:
        print(message)
        sent_messages.append(message)

sent_messages = []
send_messages(messages, sent_messages)

print("\nMessaggi inviati:")
for message in sent_messages:
    print(message)


#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

def send_messages(messages, sent_messages):
  
    for message in messages[:]:
        print(message)
        sent_messages.append(message)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nMessaggi:")
for message in messages:
    print(message)

print("\nMessaggi inviati:")
for message in sent_messages:
    print(message)
    
#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

    
def ordina_panino(*ingredienti):
   
    print("voglio un panino ordinato con i seguenti ingredienti:")
    for ingrediente in ingredienti:
        print("- " + ingrediente)

ordina_panino("Prosciutto", "Formaggio")
ordina_panino("Hamburger", "Insalata", "Pomodoro")
ordina_panino("Salame", "Cipolla", "Peperoni", "Ketchup")    


#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def crea_profilo(nome, cognome, eta, capelli, peso):
   
    profilo = f"{nome} {cognome}, età {eta}, capelli {capelli}, peso {peso}"
    return profilo

profilo_utente = crea_profilo("Germano", "Mosconi", 60, "castani", 90)
print(profilo_utente)




#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 


def make_car(manufacturer, model, **kwargs):
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(kwargs)
    return car_info

car = make_car('delorean', 'outback', color='orange', tow_package=True)
print(car)



#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

#il prossimo lo devo un po' emulare perchè ho un problema con github da casa :

# printing_functions.py

def print_models(models):
    
    for model in models:
        print("Stampo il modello:", model)

def show_completed_models(completed_models):
   
    print("\nI seguenti modelli sono stati stampati:")
    for model in completed_models:
        print(model)


def print_cars(cars):
    """Stampa le informazioni sulle auto da stampare."""
    for car in cars:
        print("Stampo le informazioni sull'auto:", car)


def show_completed_cars(completed_cars):
  
    print("\nLe seguenti informazioni sulle auto sono state stampate:")
    for car in completed_cars:
        print(car)


from printing_functions import print_cars, show_completed_cars

# Lista delle auto in print
unprinted_cars = [
    {'manufacturer': 'Toyota', 'model': 'Camry', 'color': 'blue'},
    {'manufacturer': 'Honda', 'model': 'Civic', 'color': 'red'},
    {'manufacturer': 'Ford', 'model': 'Fusion', 'color': 'silver'}
]

completed_cars = []

print_cars(unprinted_cars)
show_completed_cars(completed_cars)

#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *

#lo rifaccio in classe .


#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.

def display_message():

    print("In questo capitolo sto cercando di imparare a definire e sopratutto utilizzare le funzioni in Python. Nelle pause, consiglio un disco a tema con un libro")

display_message()

def favorite_book(title):
   
    print("Uno dei miei libri preferiti è", title)
    if title == "Alice nel Paese delle Meraviglie":
        print("Il mio album musicale preferito associato è Dark Side of the Moon dei Pink Floyd")
    elif title == "Il Piccolo Principe":
        print("Il mio album musicale preferito associato è Sgt. Pepper's Lonely Hearts Club Band dei Beatles")
    elif title == "Harry Potter":
        print("Il mio album musicale preferito associato è 2112 dei Rush")
    else:
        print("Mi dispiace, ma non ho un album musicale che  associo a questo libro.")

# a seconda del libro
favorite_book("Alice nel Paese delle Meraviglie")
favorite_book("Il Piccolo Principe")
favorite_book("Harry Potter")



