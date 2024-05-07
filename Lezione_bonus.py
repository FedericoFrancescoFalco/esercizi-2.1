#Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. 
#Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, 
#a seconda di quale sia più favorevole al giocatore in quel momento. Dato un elenco di valori delle carte che rappresentano una mano di blackjack,
# scrivi una funzione per determinare il valore totale della mano.


def blackjack_hand_total(cards: list[int]) -> int:
    total = sum(cards)
    if total>21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
            return sum(cards)
    else:
        return total
    

#Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

#1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
#2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
#3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

#Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

#Esempio:

#construct_rectangle(4)

#L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
#Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. 
#Quindi la lunghezza L è 2 e la larghezza W è 2.
def construct_rectangle(area: float) -> list[float]:
    min_diff = area - 1
    result = [area, 1]
    
    for i in range(2, int(area**0.5) + 1):
        if area % i == 0:
            j = area // i
            if j >= i and j - i < min_diff:
                min_diff = j - i
                result = [j, i]
    return result


#Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. 
#Restituisce l'elenco riorganizzato.

def even_odd_pattern(nums: list[int]) -> list[int]:
    pari = [x for x in nums if x% 2 == 0]
    dispari = [x for x in nums if x% 2 != 0]
    ritorna = pari+dispari
    return ritorna
    

#Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative 
#comuni stop_words e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente 
#(ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    word: str = ""
    Text: dict = {}
    for char in text:
        if char in [" ", ".", ",", ":", ";", "!", "?"]:
            if word is not stopwords and word !="":
                if word not in Text.keys():
                    Text[word] = 1
                else:
                    Text[word] +=1
            word = ""
        else:
            word += char.lower()
    return Text

#

def is_subsequence(s: str, t: str) -> bool:
   if len(s) > len(t):
       return False
    return s in t



    def ugly_number(num: int) -> bool:
    if num <= 0:
        return False
        
    for factor in [2, 3, 5]:
        while num % factor == 0:
            num //= factor
    return num == 1