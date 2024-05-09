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