class Prodotto:
    def __init__(self, nome: str, quantità: int, prezzo: float):
        self.nome: str = nome
        self.quantità: int = quantità
        self.prezzo: float = prezzo

    def __str__(self):
        return f"{self.nome} - Quantità: {self.quantità}, Prezzo: {self.prezzo:.2f}€"


class Magazzino:
    def __init__(self):
        self.prodotti: dict[str, Prodotto] = {}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome in self.prodotti:
            self.prodotti[prodotto.nome].quantità += prodotto.quantità
            self.prodotti[prodotto.nome].prezzo = prodotto.prezzo 
        else:
            self.prodotti[prodotto.nome] = prodotto
        print(f"Prodotto {prodotto.nome} aggiunto al magazzino. Quantità attuale: {self.prodotti[prodotto.nome].quantità}")

    def cerca_prodotto(self, nome: str) -> Prodotto:
        prodotto = self.prodotti.get(nome, None)
        if prodotto:
            print(f"Prodotto trovato: {prodotto}")
        else:
            print("Prodotto non trovato.")
        return prodotto

    def verifica_disponibilità(self, nome: str) -> str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto and prodotto.quantità > 0:
            return f"Il prodotto {nome} è disponibile. Quantità: {prodotto.quantità}, Prezzo: {prodotto.prezzo:.2f}€"
        else:
            return f"Il prodotto {nome} non è disponibile."

# specifico il magazzino
magazzino = Magazzino()

# aggiungo prodotti al magazzino
magazzino.aggiungi_prodotto(Prodotto("Ananas", 50, 2.50))
magazzino.aggiungi_prodotto(Prodotto("Fragole", 30, 3.00))

# Ricerco un un prodotto
magazzino.cerca_prodotto("Ananas")

# Verifico la disponibilità di un prodotto
print(magazzino.verifica_disponibilità("Banana"))
print(magazzino.verifica_disponibilità("Arancia"))
