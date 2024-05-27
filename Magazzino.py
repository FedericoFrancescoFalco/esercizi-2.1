
#Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

#Definisci una classe Prodotto con i seguenti attributi: nome (stringa)quantità (intero)Definisci una classe Magazzino con i seguenti metodi:aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.


class Prodotto:
    def __init__(self, nome: str, quantità: int):
        self.nome: str = nome
        self.quantità: int = quantità

class Magazzino:
    def __init__(self):
        self.prodotti: dict[str, Prodotto] = {}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome in self.prodotti:
            self.prodotti[prodotto.nome].quantità += prodotto.quantità
        else:
            self.prodotti[prodotto.nome] = prodotto
        print(f"Prodotto {prodotto.nome} aggiunto al magazzino. Quantità attuale: {self.prodotti[prodotto.nome].quantità}")

    def cerca_prodotto(self, nome: str) -> Prodotto:
        prodotto = self.prodotti.get(nome, None)
        if prodotto:
            print(f"Prodotto trovato: {prodotto.nome}, Quantità: {prodotto.quantità}")
        else:
            print("Prodotto non trovato.")
        return prodotto

    def verifica_disponibilità(self, nome: str) -> str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto and prodotto.quantità > 0:
            return f"Il prodotto {nome} è disponibile. Quantità: {prodotto.quantità}"
        else:
            return f"Il prodotto {nome} non è disponibile."

# Esempio di utilizzo
if __name__ == "__main__":
    magazzino = Magazzino()

    # Aggiungo prodotti al magazzino
    magazzino.aggiungi_prodotto(Prodotto("Ananas", 50))
    magazzino.aggiungi_prodotto(Prodotto("Fragole", 30))

    # Cerco un prodotto
    magazzino.cerca_prodotto("Ananas")

    # Verifico la disponibilità di un prodotto
    print(magazzino.verifica_disponibilità("Banana"))
    print(magazzino.verifica_disponibilità("Arancia"))