# -*- coding: utf-8 -*-
"""
Created on Sat May  3 02:27:07 2025

@author: saad saeed minhas
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod   
    def make_sound(self):
        pass
    def feed(self):
        print(f"{self.name} is eating")
        
class Cow(Animal):
    def make_sound(self):
        return f'{self.name} says Moo'

    def milk(self):
        return f'{self.name} is giving milk'

class Chicken(Animal):
    def make_sound(self):
        return f'{self.name} says Cluck'

    def lay_egg(self):
        return f'{self.name} is laying eggs'

class Sheep(Animal):
    def make_sound(self):
        return f'{self.name} says Baa'

    def shear(self):
        return f'{self.name} is being sheared'

cow = Cow('Bessie', 55)
cow.make_sound()
cow.feed()
cow.milk()