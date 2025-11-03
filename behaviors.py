from abc import ABC, abstractmethod

# FlyBehavior Interface
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self, duck_name: str):
        pass 

# Concrete classes
class FlyWithWings(FlyBehavior):
    def fly(self, duck_name: str):
        print(f"I am a {duck_name}, I can fly with a wing")

class NoFly(FlyBehavior):
    def fly(self, duck_name: str):
        print(f"I am a {duck_name}, I can't fly")

# QuackBehavior Interface
# LoudQuack (for Mallard)
# QuackToBoat (for San Antonio Duck)
# SquickSound (for Rubber Duck)
# MuteQuack (for Decoy Duck)

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self, duck_name: str):
        pass

class LoudQuack(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can quack")

class QuackToBoat(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can quack to boat?")

class SquickSound(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can squick but I can't quack")
    
class MuteQuack(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can't quack or squick")    
