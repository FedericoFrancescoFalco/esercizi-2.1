class Person:
    def __init__(self, name: str, surname: str, birth_date : str , birth_place : str, gender : str) -> None:
    
        
        self.name: str = name
        self.surname: str = surname
        self.birth_date: str = birth_date
        self.birth_place: str = birth_place
        self.gender: str = gender
        self.ssn : str = self.compute.ssn()

    def get_name(self):

        return self.name
    
    def set_name(self, name: str):

        raise Exception("You cannot modify the name!")
    
    def get_ssn(self):

        return self.ssn
    
    def set_ssn(self, ssn: str) -> None:


        self.ssn = ssn
        raise Exception("You cannot modify!")

def get_ssn(self):
    return self.ssn

def set_ssn(self, ssn: str):



    self.ssn = ssn

def compute_ssn(self) -> bool:
    first_three_name_char = self.name[:3]
    last_three_name_char = self.surname[:3]
    self.ssn = first_three_name_char + last_three_name_char


person_1: Person = Person(name = "Federico", surname = "Falco", ssn = "FLC")


#esercizio

person_2: Person = Person(name = "Francesco", surname = "Falco", ssn = "FLCGHERNSTRN")

queue: list = [person_1 , person_2]

for person in queue:
    print(person.get_ssn())