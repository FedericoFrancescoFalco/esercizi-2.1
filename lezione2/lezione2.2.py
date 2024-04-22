#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

person_name = "Federico"
print("ciao,", person_name + "! Vuoi imparare un po' di coding oggi?")



# 2-4. Name Cases: Use a variable to represent a person’s name, and then 
#      print that person’s name in lowercase, uppercase, and title case.
# Define the variable for the person's name
person_name = "federico"

print("Lowercase:", person_name.lower())
print("Uppercase:", person_name.upper())
print("Title Case:", person_name.title())



# 2-5. Famous Quote: Find a quote from a famous person you admire. 
#      Print the quote and the name of its author. Your output should look something like the following, 
#      including the quotation marks: Albert Einstein once said, 
#      “A person who never made a mistake never tried anything new.”


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s 
#      name using a variable called famous_person. Then compose your message and represent 
#      it with a new variable called message. Print your message. 
frase_famosa = "It means so much to me when pretend becomes real"
persona_famosa = "John Frusciante"
messaggio= f"Una volta {persona_famosa} disse:{frase_famosa}"
print(messaggio)


# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#      Assign the value 'python_notes.txt' to a variable called filename. 
#      Then use the removesuffix() method to display the filename without the file extension, 
#      like some file browsers do.
filename = 'python_notes.txt'
filename_senza_estensione = filename.removesuffix('.txt')
print("Nome del file senza estensione:", filename_senza_estensione)


# 3-1. Names: Store the names of a few of your friends in a list called names. 
#      Print each person’s name by accessing each element in the list, one at a time.
lista_amici = ["luigi","luciano","alberto"]
print(lista_amici[0])
print(lista_amici[1])
print(lista_amici[2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of 
#      just printing each person’s name, print a message to them. 
#      The text of each message should be the same, but each message should be personalized with 
#      the person’s name.
lista_amici = ["luigi", "luciano", "alberto"]
messaggio_saluto = "Ciao, {}! Ricordati di fare gli esercizi di Python!"

print(messaggio_saluto.format(lista_amici[0]))
print(messaggio_saluto.format(lista_amici[1]))
print(messaggio_saluto.format(lista_amici[2]))



# 3-3. Your Own List: Think of your favorite mode of transportation, 
#      such as a motorcycle or a car, and make a list that stores several examples. 
#      Use your list to print a series of statements about these items, such as 
#      “I would like to own a Honda motorcycle.”
Lista_Trasporti = ["auto", "bus", "treno"]
messaggio_motivazione_uno = "mi piacerebbe, ma non ho la patente per l'"
messaggio_motivazione_due = "risparmio molto in"
messaggio_motivazione_tre = "mi rilassa viggiare in"
print(messaggio_motivazione_uno.format(Lista_Trasporti[0]))
print(messaggio_motivazione_due.format(Lista_Trasporti[1]))
print(messaggio_motivazione_tre.format(Lista_Trasporti[2]))


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#      Make a list that includes at least three people you’d like to invite to dinner. 
#      Then use your list to print a message to each person, inviting them to dinner.
Lista_Inviti = ["David_Bowie", "Kate_Bush", "Robert_Smith" ]
Messaggio_Invito_uno = "sarei lieto di invitarla a cena a discutere di Cinema"
Messaggio_Invito_due = "mi piacerebbe invitarla a cena per parlare di come ha composto i suoi dischi"
Messaggio_Invito_tre = "gradirei venisse a cena a casa mia per mostrarle il libro scritto su di lei"
Saluto_uno = "Signor"
Saluto_due = "Signora"
Saluto_tre = "Lo metto solo per far arrabbiare Adinolfi"
print(Saluto_uno + " " + Lista_Inviti[0] + ", " + Messaggio_Invito_uno)
print(Saluto_due + " " + Lista_Inviti[1] + ", " + Messaggio_Invito_due)
print(Saluto_tre + " " + Lista_Inviti[2] + ", " + Messaggio_Invito_tre)

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
#      so you need to send out a new set of invitations. You’ll have to think of someone else to invite:
#
#      • Start with your program from Exercise 3-4. Add a print() 
#        call at the end of your program, stating the name of the guest who can’t make it.
#      • Modify your list, replacing the name of the guest who can’t make it with the name of 
#        the new person you are inviting.
#      • Print a second set of invitation messages, one for each person who is still in your list.
Lista_Inviti = ["David_Bowie", "Kate_Bush", "Robert_Smith" ]
Messaggio_Invito_uno = "sarei lieto di invitarla a cena a discutere di Cinema"
Messaggio_Invito_due = "mi piacerebbe invitarla a cena per parlare di come ha composto i suoi dischi"
Messaggio_Invito_tre = "gradirei venisse a cena a casa mia per mostrarle il libro scritto su di lei"
Saluto_uno = "Signor"
Saluto_due = "Signora"
Saluto_tre = "Lo metto solo per far arrabbiare Adinolfi"
Cancellazione = "purtroppo non potrà venire"
print(Saluto_uno + " " + Lista_Inviti[0] + ", " + Messaggio_Invito_uno)
print(Saluto_due + " " + Lista_Inviti[1] + ", " + Messaggio_Invito_due)
print(Saluto_uno + " " + Lista_Inviti[2] + ", " + Messaggio_Invito_tre)
print(Cancellazione.format(Lista_Inviti[2]))
Lista_Inviti.remove("Robert_Smith")
Lista_Inviti.append("Ian_Curtis")
Messaggio_Invito_quattro = "sono felice di incontrarla stasera"
print(Saluto_uno + " " + Lista_Inviti[2] + ", " + Messaggio_Invito_quattro)
print(Saluto_uno + " " + Lista_Inviti[0] + ", " + Messaggio_Invito_uno)
print(Saluto_due + " " + Lista_Inviti[1] + ", " + Messaggio_Invito_due)

# 3-6. More Guests - You just found a bigger dinner table, so now more space is available. 
#      Think of three more guests to invite to dinner:
#
#      • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
#        informing people that you found a bigger table.
#      • Use insert() to add one new guest to the beginning of your list.
#      • Use insert() to add one new guest to the middle of your list.
#      • Use append() to add one new guest to the end of your list.
#      • Print a new set of invitation messages, one for each person in your list.
Messaggio_Invito_Cinque = "vi informo che abbiamo trovato un tavolo più grande"
print(Lista_Inviti[0] +", "+ Lista_Inviti[1] + ", " + Lista_Inviti[2]+" " + Messaggio_Invito_Cinque)
Lista_Inviti.insert(1,"Miriam_Leone")
Lista_Inviti.insert(2,"Howard_Lovecraft")
Lista_Inviti.append("Bruce_Dickinson")
print(f"mi dispiace {Lista_Inviti.pop(0)} ma si sono verificati alcuni imprevisti")
print(f"mi dispiace {Lista_Inviti.pop(1)} ma si sono verificati alcuni imprevisti")
print(f"mi dispiace {Lista_Inviti.pop(2)} ma si sono verificati alcuni imprevisti")
print(Lista_Inviti)

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in 
#      time for the dinner, and now you have space for only two guests:
#
#      • Start with your program from Exercise 3-6. Add a new line that prints a message saying 
#        that you can invite only two people for dinner.
#      • Use pop() to remove guests from your list one at a time
#        until only two names remain in your list. Each time you pop a name from your list, 
#        print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#      • Print a message to each of the two people still on your list, letting them know they’re still invited.
#      • Use del to remove the last two names from your list, so you have an empty list. 
#      Print your list to make sure you actually have an empty list at the end of your program.


# 3-8. Seeing the World - Think of at least five places in the world you’d like to visit:
#
#      • Store the locations in a list. Make sure the list is not in alphabetical order.
#      • Print your list in its original order. Don’t worry about printing the list neatly; 
#        just print it as a raw Python list.
#      • Use sorted() to print your list in alphabetical order without modifying the actual list.
#      • Show that your list is still in its original order by printing it.
#      • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#      • Show that your list is still in its original order by printing it again.
#      • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#      • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#      • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that 
#        its order has been changed.
#      • Use sort() to change your list so it’s stored in reverse-alphabetical order.
#      Print the list to show that its order has changed.
Lista_Luoghi = ["Colosseo","Partenone","Fontana_di_Trevi","Torre_Effeil", "Lupa_Capitolina"]
print(Lista_Luoghi)
Lista_Luoghi.sort()
print(Lista_Luoghi)
Lista_Luoghi.sort(reverse=True)
print(Lista_Luoghi)
Lista_Luoghi.reverse()
print(Lista_Luoghi)
Lista_Luoghi.reverse()
print(Lista_Luoghi)
# 3-9. Dinner Guests - Working with one of the programs from Exercises 3, use len() to print 
#      a message indicating the number of people you’re inviting to dinner.
num_invitati = len(Lista_Inviti)
print("stai invitando {} persone".format(num_invitati))

# 3-10. Every Function - Think of things you could store in a list. 
#       For example, you could make a list of mountains, rivers, countries, 
#       cities, languages, or anything else you’d like. Write a program that creates 
#       a list containing these items and then uses each function introduced in this chapter at least once.


print(Lista_Luoghi)
Lista_Luoghi.sort()
Lista_Luoghi.reverse()
Numero_Luoghi = len(Lista_Luoghi)
print(Lista_Luoghi)
print(Numero_Luoghi)
Lista_Luoghi.insert (len(Lista_Luoghi)//2, "Altare_della_Patria")
print(Lista_Luoghi)
Lista_Luoghi.remove("Partenone")
Lista_Luoghi.append("Piazza_Navona")
print(f"toglierei la {Lista_Luoghi.pop(2)} ci sono già stato")

# 6-1. Person - Use a dictionary to store information about a person you know. 
#      Store their first name, last name, age, and the city in which they live. 
#      You should have keys such as first_name, last_name, age, and city. 
#      Print each piece of information stored in your dictionary.
Persona = {
    "Nome" : "John" ,
    "Cognome" : "Frusciante" ,
    "Età" : "cinquantacinque" ,
    "Nato a" : "New York",
 }
print ( "Nome:" , Persona["Nome"])
print ( "Cognome:" , Persona["Cognome"])
print ( "Età:" , Persona["Età"])
print ( "Nato a:" , Persona["Nato a"])


# 6-2. Favorite Numbers - Use a dictionary to store people’s favorite numbers. 
#      Think of five names, and use them as keys in your dictionary. 
#      Think of a favorite number for each person, and store each as a value in your dictionary. 
#      Print each person’s name and their favorite number. For even more fun, 
#      poll a few friends and get some actual data for your program.
Età_dei_componenti_della_band = {
"Antony" : 61 ,
"Flea" : 62 ,
"Chad" : 63 ,
"Frusciante" : 54 ,
}
for Persone , Età in Età_dei_componenti_della_band.items():
    print(Persone + "la sua età è'", Età)

# 6-3. Glossary - A Python dictionary can be used to model an actual dictionary. 
#      However, to avoid confusion, let’s call it a glossary:
#
#      • Think of five programming words you’ve learned about in the previous chapters. 
#        Use these words as the keys in your glossary, and store their meanings as values.
#      • Print each word and its meaning as neatly formatted output. 
#        You might print the word followed by a colon and then its meaning, 
#        or print the word on one line and then print its meaning indented on a second line. 
#      Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

Dizionario_1 = {"Append": "Inserisce una variabile a fine della lista"}
Dizionario_2 = {"Remove": "Cancella una variabile nella lista in un ordine casuale"}
Dizionario_3 = {"Len": "Indica quanti elementi ci sono numericamente nella lista"}
Dizionario_4 = {"Sort": "Indicizza in ordine alfabetico tutti gli elementi della lista"}
Dizionario_5 = {"Reverse": "Sistema la lista in ordine inverso"}
Lista_parole: list = [Dizionario_1, Dizionario_2, Dizionario_3, Dizionario_4, Dizionario_5]

for dizionario in Lista_parole:
    for k, v in dizionario.items():
        print(f"{k}\n{v}")
    print("")

# 6-7. People - Start with the program you wrote for Exercise 6-1. 
#      Make two new dictionaries representing different people, and store all three 
#      dictionaries in a list called people. Loop through your list of people. 
#      As you loop through the list, print everything you know about each person.
Persona_1 = {"Nome" : "Mike" ,"Cognome" : "Patton" ,"Età" : "cinquantacinque" ,"Nato a" : "Eureka"}
Persona_2 = {"Nome" : "James" ,"Cognome" : "Hetfield" ,"Età" : "sessantuno" ,"Nato a" : "San Francisco"}

gente = [Persona_1, Persona_2]
print(gente)

# 6-8. Pets - Make several dictionaries, where each dictionary represents a different pet. 
#      In each dictionary, include the kind of animal and the owner’s name. 
#      Store these dictionaries in a list called pets. Next, loop through your list and as
#      you do, print everything you know about each pet. 
Specie = {"Pet_1": "Gatto", "Pet_2": "Cane", "Pet_3": "Iguana"}
Proprietario = {"Pet_1": "Vincenzo", "Pet_2": "Sharon", "Pet_3": "Vladimiro"}

Pet_1 = {"Pet_1":Specie["Pet_1"], "Per_1":Proprietario["Pet_1"]}
Pet_2 = {"Pet_2":Specie["Pet_2"],"Per_2":Proprietario["Pet_2"]}
Pet_3 = {"Pet_3":Specie["Pet_3"],"Per_2":Proprietario["Pet_3"]}

Pets: list = [Pet_1, Pet_2, Pet_3]
for dizionario in Pets:
    for k, v in dizionario.items():
        print(f"{k}\n{v}") 

# 6-9. Favorite Places - Make a dictionary called favorite_places. 
#      Think of three names to use as keys in the dictionary, and store one to three 
#      favorite places for each person. To make this exercise a bit more interesting, 
#      ask some friends to name a few of their favorite places. 
#      Loop through the dictionary, and print each person’s name and their favorite places.
Luoghi_villeggiatura = {"Piazza_San_Marco": "Marco", "Vaticano" : "Daniele", "Piazza_di_Spagna": "Giuseppe"}
print(Luoghi_villeggiatura)


# 6-10. Favorite Numbers - Modify your program from Exercise 6-2 so each person can have 
#       more than one favorite number. Then print each person’s name along with their favorite numbers.



# 6-11. Cities - Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#       Create a dictionary of information about each city and include the country that the city is in, 
#       its approximate population, and one fact about that city. The keys for each city’s dictionary should 
#       be something like country, population, and fact. Print the name of each city and all of the 
#       information you have stored about it.
cities = { "New York": { "country": "United States", "population": "8.3 million", "fact": "New York City is home to the largest Polish population outside of Poland." }, 
          "Paris": { "country": "France", "population": "2.1 million", "fact": "The Eiffel Tower was originally intended for Barcelona, Spain, but the project was rejected and moved to Paris." }, 
          "Tokyo": { "country": "Japan", "population": "13.5 million", "fact": "Tokyo is the most populous metropolitan area in the world." } }

for city, city_info in cities.items(): print("\nCity:", city) 
print("Country:", city_info["country"]) 
print("Population:", city_info["population"]) 
print("Fact:", city_info["fact"])


# 6-12. Extensions - We’re now working with examples that are complex enough that they can be 
#       extended in any number of ways. Use one of the example programs from this chapter, 
#       and extend it by adding new keys and values, changing the context of the program, 
#       or improving the formatting of the output.
# Create a dictionary of items and their prices
items = {
    'mela': 0.99,
    'banana': 0.59,
    'arancia': 0.79,
    'uva': 2.99,
    'melone': 4.99
}

print("Items and their prices:")
for item, price in items.items():
    print(f"{item.capitalize()}: €{price}")

total_cost = sum(items.values())
print(f"\nTotal cost of all items: €{total_cost}")

