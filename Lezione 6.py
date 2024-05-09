from typing import Tuple

class Person:
    
    def __init__(self, name: str, surname: str, birth_date : str , birth_place : str, gender : str) -> None:
    
        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender: str = gender
        self._ssn : str = self.compute_ssn()

    def get_name(self):

        return self.name
    
    def set_name(self, name: str):

        raise Exception("You cannot modify the name!")
    
    def get_ssn(self):

        return self._ssn
    
    def set_ssn(self, ssn: str) -> None:


        self.ssn = ssn
        raise Exception("You cannot modify!")

    def get_ssn(self):
        return self._ssn

    def set_ssn(self, ssn: str):

        self._ssn = ssn

    def compute_ssn(self) -> bool:
        first_three_name_char = self._name[:3]
        last_three_name_char = self._surname[-3:]
        self._ssn = first_three_name_char + last_three_name_char
        return self._ssn


person_1: Person = Person(name = "Federico", surname = "Falco", birth_date = "31/7/1985" , birth_place = "Roma" , gender = "male" )


#esercizio

person_2: Person = Person(name = "Francesco", surname = "Falco",  birth_date = "21/7/1995" , birth_place = "Napoli" , gender = "male")

queue: list = [person_1 , person_2]

for person in queue:
    print(person.get_ssn())