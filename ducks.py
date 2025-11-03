from abc import ABC, abstractmethod
from behaviors import FlyBehavior, QuackBehavior

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
        self.fly_behavior.fly(self.class___.__name__)

    def perform_quack(self):
        self.quack_behavior.quack(self.class___.__name__)

    def swim(self):
        print(f"I am a {self.__class__.__name__}, I can paddle and swim.")

    def walk(self):
        print(f"I am a {self.__class__.__name__}, I can walk")

# Subclasses
class San_Antonio(Duck):
    def speak(self):
        pass

    def swim(self):
        pass

    def fly(self):
        pass

class Mallard(Duck):
    def speak(self):
        pass

    def swim(self):
        pass

    def fly(self):
        pass

class Decoy(Duck):
    def speak(self):
        pass

    def swim(self):
        pass

    def fly(self):
        pass

class Rubber(Duck):
    def speak(self):
        pass

    def swim(self):
        pass

    def fly(self):
        pass