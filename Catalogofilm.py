#Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. 
#Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

#Classe: MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.
#Metodi:add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
#Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.
#remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
#list_directors(): Elenca tutti i registi presenti nel catalogo.
#get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.
#search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
#Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.






class MovieCatalog:
    def __init__(self):
        self.catalog = {}  

    def add_movie(self, director_name, movies):
        
        if director_name not in self.catalog:
            self.catalog[director_name] = []  
        if isinstance(movies, list):
            self.catalog[director_name].extend(movies)  
        else:
            self.catalog[director_name].append(movies)  

    def remove_movie(self, director_name, movie_name):
        
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name) 
                if not self.catalog[director_name]: 
                    del self.catalog[director_name]
            else:
                print(f"Il film '{movie_name}' non è nella filmografia del regista '{director_name}'.")
        else:
            print(f"Il regista '{director_name}' non è nel catalogo.")

    def list_directors(self):
        
        return list(self.catalog.keys())

    def get_movies_by_director(self, director_name):
        
        if director_name in self.catalog:
            return self.catalog[director_name]
        else:
            return f"Il regista '{director_name}' non è nel catalogo."

    def search_movies_by_title(self, title):
        
        result = {}
        for director, movies in self.catalog.items():
            matching_movies = [movie for movie in movies if title.lower() in movie.lower()]
            if matching_movies:
                result[director] = matching_movies
        if result:
            return result
        else:
            return f"Nessun film trovato con la frase '{title}' nel titolo."


catalogo = MovieCatalog()


catalogo.add_movie("Christopher Nolan", ["Batman", "Interstellar", "Oppenahimer"])
catalogo.add_movie("David Lynch", ["Strade Perdute", "Velluto Blu", "Erasehead"])
catalogo.add_movie("Christopher Nolan", "Memento")  


catalogo.remove_movie("David Lynch", "Velluto Blu")


print("Registi nel catalogo:", catalogo.list_directors())


print("Film di Christopher Nolan:", catalogo.get_movies_by_director("Christopher Nolan"))


print("Film che contengono 'Strade Perdute':", catalogo.search_movies_by_title("Strade Perdute"))
