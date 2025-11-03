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
class QuackBehavior(ABC):
    @abstractmethod
    def quack(self, duck_name: str):
        pass

# LoudQuack (for Mallard)
class LoudQuack(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can quack")

# QuackToBoat (for San Antonio Duck)
class QuackToBoat(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can quack to boat?")

# SquickSound (for Rubber Duck)
class SquickSound(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can squick but I can't quack")
    
# MuteQuack (for Decoy Duck)
class MuteQuack(QuackBehavior):
    def quack(self, duck_name):
        print(f"I am a {duck_name}, I can't quack or squick")    
