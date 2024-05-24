#Sistema di Prenotazione Cinema
#Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
#Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
#Classi:
#Film: Rappresenta un film con titolo e durata.
 
#Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

#Metodi:
#aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

#Test case:
#Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
#Un cliente sceglie un film e prenota un certo numero di posti.
#Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:
    def __init__(self, title: str, runtime: float):
        self.title = title
        self.runtime = runtime

class Sala:
    def __init__(self, room_number: int, movie: Film, total_seats: int):
        self.room_number = room_number
        self.movie = movie
        self.total_seats = total_seats
        self.booked_seats = 0

    def prenota_posti(self, num_posti: int) -> str:
        if self.booked_seats + num_posti <= self.total_seats:
            self.booked_seats += num_posti
            return f"Prenotazione confermata per {num_posti} posti per il film {self.movie.title}."
        else:
            return "Ci dispiace, non ci sono abbastanza posti disponibili."

    def posti_disponibili(self) -> int:
        return self.total_seats - self.booked_seats

class Cinema:
    def __init__(self):
        self.sale = []

    def aggiungi_sala(self, sala: Sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.sale:
            if sala.movie.title == titolo_film:
                return sala.prenota_posti(num_posti)
        return f"Film {titolo_film} non trovato."

# Film
film1 = Film("Titanic", 120)
film2 = Film("Godzilla", 90)

# Sale
sala1 = Sala(1, film1, 100)
sala2 = Sala(2, film2, 150)

# Cinema e Sla
cinema = Cinema()
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)


print(cinema.prenota_film("Titanic",200))
