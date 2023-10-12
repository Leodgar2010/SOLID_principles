# Dependency Inversion Principle

from abc import ABC, abstractmethod
from random import randint


class Cannon:
    def __init__(self, ammo):
        self.ammo = ammo

    def load_cannon(self):
        load = self.ammo.get_ammo()
        print (f"Cannon has {load} ammo")


class Storage(ABC):
    @abstractmethod
    def get_ammo(self):
        pass

class Crate(Storage):
    def get_ammo (self):
        return randint (4,8)

class Pile (Storage):
    def get_ammo(self):
        return randint(1, 3)

if __name__ == "__main__":
    cannon = Cannon(Crate())
    cannon.load_cannon()
    cannon2=Cannon(Pile())
    cannon2.load_cannon()

