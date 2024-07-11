class Car:

    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def set(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):
        self.__protected()

    def __protected(self):
        print("Transportation ", self.model, " can drive at the speed", self.speed, " of everyone ", self.wheels, " wheels!")


class Motorcycle(Car):
    engine = "Default"

    def getAll(self):
        super().getAll()
        print("Its engine", self.engine)

    def change(self, engine):
        self.engine = engine
        print("The motorcycle engine is set up like: " + engine)

    def __init__(self, wheels, model, speed, engine):
        self.engine = engine
        super(Motorcycle, self).__init__(wheels, model, speed)


shkoda = Car(4, "Shkoda", 125.45)
shkoda.getAll()

audi = Car(4, "Audi", 250.9)
audi.getAll()

print("")

harley = Motorcycle(2, "Harley Davidson", 200, "Powerfull")
harley.getAll()