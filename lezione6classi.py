#Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f" Con {self.restaurant_name} mangerai la vera cucina  {self.cuisine_type} ")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} è aperto oggi.")

restaurant = Restaurant("Sora Lella", "romana")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant.describe_restaurant()
restaurant.open_restaurant()


#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.


class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f" Con {self.restaurant_name} mangerai la vera cucina  {self.cuisine_type} ")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} è aperto oggi.")

restaurant1 = Restaurant("Sora Lella", "romana")
restaurant2 = Restaurant("Ciumbia", "brianzola")
restaurant3 = Restaurant("Vesuvio", "napoletana")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()






#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

class User:
    
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def greet_user(self):
        print(f"Ragazzi, vi presento {self.first_name} {self.last_name}, ha {self.age} e viene dalla bellissima città di {self.city}. Forza, salutate {self.first_name}")

    def describe_user(self):
        print(f"Il nome è {self.first_name}, il cognome è {self.last_name}, la sua età è {self.age}, nato a {self.city}")

user1 = User("Mario", "Magnotta", 30, "Roma")
user2 = User("Lindo", "Ferretti", 25, "Milano")


user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()

#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"Con {self.restaurant_name} mangerai la vera cucina {self.cuisine_type}. Oggi sono stati serviti {self.number_served} clienti.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} è aperto oggi.")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, increment):
        self.number_served += increment



restaurant = Restaurant("Sora Lella", "romana")


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant.describe_restaurant()
restaurant.open_restaurant()


print(f"Numero di clienti serviti: {restaurant.number_served}")
restaurant.set_number_served(100)
print(f"Numero di clienti serviti dopo l'aggiornamento: {restaurant.number_served}")


restaurant.increment_number_served(25)
print(f"Numero di clienti serviti dopo incremento: {restaurant.number_served}")


#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0 
    
    def greet_user(self):
        print(f"Ragazzi, vi presento {self.first_name} {self.last_name}, ha {self.age} e viene dalla bellissima città di {self.city}. Forza, salutate {self.first_name}")

    def describe_user(self):
        print(f"Il nome è {self.first_name}, il cognome è {self.last_name}, la sua età è {self.age}, nato a {self.city}")
    
    def increment_login_attempts(self):
        
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        
        self.login_attempts = 0


user1 = User("Mario", "Magnotta", 30, "Roma")


user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()


print(f"Login attempts: {user1.login_attempts}")  


user1.reset_login_attempts()


print(f"Login attempts after reset: {user1.login_attempts}")  


user2 = User("Lindo", "Ferretti", 25, "Milano")
user2.greet_user()
user2.describe_user()

#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Con {self.restaurant_name} mangerai la vera cucina {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} è aperto oggi.")

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)  
        self.flavors = flavors  
    
    def display_flavors(self):
       
        print("I gusti di gelato disponibili sono:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("Gelateria Zerocalcare", "gelato", ["vaniglia", "cioccolato", "fragola", "limone", "stracciatella"])

ice_cream_stand.display_flavors()

#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 

class User:
    
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def greet_user(self):
        print(f"Ragazzi, vi presento {self.first_name} {self.last_name}, ha {self.age} e viene dalla bellissima città di {self.city}. Forza, salutate {self.first_name}")

    def describe_user(self):
        print(f"Il nome è {self.first_name}, il cognome è {self.last_name}, la sua età è {self.age}, nato a {self.city}")

class Admin(User):
    
    def __init__(self, first_name, last_name, age, city, privileges):
        super().__init__(first_name, last_name, age, city)  
        self.privileges = privileges  
    
    def show_privileges(self):
        
        print("I privilegi dell'amministratore sono:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin1 = Admin("Federico", "Falco", 38, "Napoli", ["può aggiungere post", "cancellare post", "bannare iscritti"])

admin1.show_privileges()

#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

class User:
    
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def greet_user(self):
        print(f"Ragazzi, vi presento {self.first_name} {self.last_name}, ha {self.age} e viene dalla bellissima città di {self.city}. Forza, salutate {self.first_name}")

    def describe_user(self):
        print(f"Il nome è {self.first_name}, il cognome è {self.last_name}, la sua età è {self.age}, nato a {self.city}")

class Privileges:
    
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        
        if self.privileges:
            print("I privilegi dell'amministratore sono:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("L'amministratore non ha privilegi.")

class Admino(User):
    
    def __init__(self, first_name, last_name, age, city, privileges=[]):
        super().__init__(first_name, last_name, age, city)  
        self.privileges = Privileges(privileges) 


admin1 = Admino("Federico", "Falco", 38, "Napoli", ["può aggiungere post", "cancellare post", "bannare iscritti"])

admin1.privileges.show_privileges()

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

# restaurant_module.py

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Con {self.restaurant_name} mangerai la vera cucina {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} è aperto oggi.")

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print("I gusti di gelato disponibili sono:")
        for flavor in self.flavors:
            print(f"- {flavor}")
            
            

  # test_restaurant.py a parte:

from restaurant_module import Restaurant, IceCreamStand


my_restaurant = Restaurant("La Trattoria", "italiana")
my_restaurant.describe_restaurant()


ice_cream_stand = IceCreamStand("Gelateria Zerocalcare", "gelato", ["vaniglia", "cioccolato", "fragola", "limone", "stracciatella"])
ice_cream_stand.display_flavors()


#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.




# test_admin.py a parte 

from user_module import Admino


admin1 = Admino("Federico", "Falco", 38, "Napoli", ["può aggiungere post", "cancellare post", "bannare iscritti"])

admin1.privileges.show_privileges()

