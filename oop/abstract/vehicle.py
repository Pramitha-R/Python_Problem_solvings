from abc import ABC ,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("your are riding the bick")

class Car(Vehicle):
    def start(self):
        print("your are riding the car")