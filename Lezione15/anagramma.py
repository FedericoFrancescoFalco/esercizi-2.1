#Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
#Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola 
#o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

print("Question 1\n")
def anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())


print(anagram("anagram","nagaram"))
print(anagram("rat", "car"))
print(anagram("silent","listen"))
print(anagram("NeurIPS","UniReps"))
print("\n")