from abc import ABC, abstractmethod
from behaviors import (
    FlyBehavior, QuackBehavior, FlyWithWings, NoFly, 
    LoudQuack, QuackToBoat, SquickSound, MuteQuack
)
# Abstract Class
class Duck(ABC):
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self):
        """Each subclass defines how it looks."""
        pass

    def perform_fly(self):
        self.fly_behavior.fly(self.__class__.__name__)

    def perform_quack(self):
        self.quack_behavior.quack(self.__class__.__name__)

    # Mallard and SA Ducks
    def swim(self):
        print(f"I am a {self.__class__.__name__}, I can paddle and swim.")

    # SA Duck only
    def walk(self):
        print(f"I am a {self.__class__.__name__}, I can walk")

# Subclasses
class San_Antonio(Duck):
    # SA Duck uses FlyWithWings and QuackToBoat
    def __init__(self):
        super().__init__(FlyWithWings(),QuackToBoat())

    def display(self):
        print(f"--- Displaying a {self.__class__.__name__} ---")

    # SA Duck can swim and walk

class Mallard(Duck):
    # Mallard Duck uses FlyWithWings and LoudQuack
    def __init__(self):
        super().__init__(FlyWithWings(),LoudQuack())

    def display(self):
        print(f"--- Displaying a {self.__class__.__name__} ---")

    # Mallard Duck can swim but can't walk
    def walk(self):
        pass

class Decoy(Duck):
    # SA Duck uses NoFLy and MuteQuack
    def __init__(self):
        super().__init__(NoFly(),MuteQuack())

    def display(self):
        print(f"--- Displaying a {self.__class__.__name__} ---")

    # Decoy Duck can't swim or walk

class Rubber(Duck):
    # Rubber Duck uses NoFLy and SquickSound
    def __init__(self):
        super().__init__(NoFly(),SquickSound())

    def display(self):
        print(f"--- Displaying a {self.__class__.__name__} ---")
        
    # Rubber Duck can't swim or walk