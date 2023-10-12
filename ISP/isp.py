# interfase suggestion

class AnimalBehavior:
    def walk(self):
        raise NotImplementedError

class FishBehavior:
    def swim(self):
        raise NotImplementedError

class Wolf(AnimalBehavior):
    def walk(self):
        pass

class Bear(AnimalBehavior):
    def walk(self):
        pass

class Cat(AnimalBehavior):
    def walk(self):
        pass

class Shark(FishBehavior):
    def swim(self):
        pass


