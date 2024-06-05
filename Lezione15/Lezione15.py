#Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
#Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola 
#o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

import unittest
from anagramma import Anagram

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        with open("Esercizio.txt", "r") as reader:
            reader.readlines()
            