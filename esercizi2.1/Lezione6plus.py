class Studente:
    def __init__(self, nome, programma_di_studio, età, genere):
        self.nome = nome
        self.programma_di_studio = programma_di_studio
        self.età = età
        self.genere = genere

    def stampa_info(self):
        print(f"Nome: {self.nome}, Programma di Studio: {self.programma_di_studio}, Età: {self.età}, Genere: {self.genere}")

# creo le istanze per studente
io = Studente("Spartaco", "Informatica", 20, "Maschio")
vicino_sinistra = Studente("Riccardo", "Fisica", 22, "Maschio")
vicino_destra = Studente("Gianfranco", "Matematica", 21, "Maschio")


io.stampa_info()
vicino_sinistra.stampa_info()
vicino_destra.stampa_info()


#Esercizio 2

class Animal:
    def __init__(self, name: str, legs: int) -> None:
        self._name: str = name
        self._legs: int = legs

    def set_legs(self, legs: int):
        self._legs = legs

    def get_legs(self) -> int:
        return self._legs

    def print_info(self):
        print(f"name: {self._name}, legs: {self._legs}")
    
animale1: Animal = Animal("Chocobo",2)
animale1.print_info()

#esercizi 3

class Cibo:
    def __init__(self, name: str, price:int, description: str):
        self._name: str = name
        self._price: int = price
        self._description : str = description
    
class Menu:
    def __init__(self, food_list: list = []):
        self._foodlist: list = food_list

    def addFood(self, food: Cibo):
        self._foodlist.append(food) 

    def remFood(self, index: int):
        del self._foodlist[index]

    def printPrices(self):
        for food in self._foodlist:
            print(food._price)

    def getAveragePrice(self) -> float:
        result:float = 0
        for food in self._foodlist:
            result = result + food._price
        result = result / len(self._foodlist)
        return result

food1: Cibo = Cibo("pizza", 100, "bona")
food2: Cibo = Cibo("hamburger", 150, "dietetico")
food3: Cibo = Cibo("ramen", 50, "scaduto")
food4: Cibo = Cibo("patata", 500, "sa di cancello")
food5: Cibo = Cibo("aragosta irachena",250 , "buona con il burro fuso")

food_list: list = [food1, food2, food3]

menu_esso: Menu = Menu(food_list)

menu_esso.addFood(food4)
menu_esso.addFood(food5)

menu_esso.remFood(2)

menu_esso.printPrices()


