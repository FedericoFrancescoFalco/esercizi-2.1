from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cerchio(Forma):
    def __init__(self, raggio: float):
        self.raggio = raggio

    def area(self) -> float:
        return math.pi * self.raggio * self.raggio

    def perimetro(self) -> float:
        return 2 * math.pi * self.raggio

class Rettangolo(Forma):
    def __init__(self, larghezza: float, altezza: float):
        self.larghezza = larghezza
        self.altezza = altezza

    def area(self) -> float:
        return self.larghezza * self.altezza

    def perimetro(self) -> float:
        return 2 * (self.larghezza + self.altezza)

cerchio = Cerchio(5.0)
print("Area del cerchio:", cerchio.area())
print("Perimetro del cerchio:", cerchio.perimetro())

rettangolo = Rettangolo(4.0, 6.0)
print("Area del rettangolo:", rettangolo.area())
print("Perimetro del rettangolo:", rettangolo.perimetro())
