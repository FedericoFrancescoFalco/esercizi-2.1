#Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
#Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
#Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.

# Classi: Libro: Rappresenta un libro con titolo, autore, stao del prestito. Il libro deve essere inizialmente disponibile (non prestato).

#Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#Metodi:
#aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
#presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

#Test Cases:
#Un amministratore della biblioteca aggiunge alcuni libri all'inventario.

#Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.

#L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
#In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = True

    def __str__(self):
        stato = "avaliable" if self.disponibile else "not avaliable"
        return f"{self.titolo} di {self.autore} ({stato})"


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f'Book "{libro.titolo}" added on stock.'

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.disponibile:
                    libro.disponibile = False
                    return f'Book "{titolo}" borrowed.'
                else:
                    return f'Book "{titolo}" not avaliable.'
        return f'Book "{titolo}" not found.'

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.disponibile:
                    libro.disponibile = True
                    return f'Book "{titolo}" re-added.'
                else:
                    return f'Book "{titolo}" re-added.'
        return f'Book "{titolo}" not found.'

    def mostra_libri_disponibili(self):
        disponibili = [libro.titolo for libro in self.catalogo if libro.disponibile]
        if disponibili:
            return "Books avaliable :\n" + "\n".join(disponibili)
        else:
            return "No book savaliable ."





biblioteca = Biblioteca()

print(biblioteca.aggiungi_libro(Libro("Guida Ragionevole al frastuono più atroce", "Lester Bangs")))
print(biblioteca.aggiungi_libro(Libro("Scar Tissue", "Anthony Kiedis")))
print(biblioteca.aggiungi_libro(Libro("Brave New World", "Aldous Huxley")))


print(biblioteca.presta_libro("Scar Tissue"))


print(biblioteca.presta_libro("Scar Tissue"))

print(biblioteca.restituisci_libro("Scar Tissue"))

print(biblioteca.mostra_libri_disponibili())


