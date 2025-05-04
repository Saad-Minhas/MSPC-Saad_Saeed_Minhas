# -*- coding: utf-8 -*-
"""
Created on Fri May  2 00:25:36 2025

@author: saad saeed minhas
"""

class Car:
    def __init__(self, owner, brand, model, engine_size):
        self.owner = owner
        self.brand = brand
        self.model = model
        self.engine_size = engine_size

    def modify_engine_size(self, new_engine_size):
        self.engine_size = new_engine_size

    def modify_owner(self, new_owner):
        self.owner = new_owner

    def get_info(self):
        return f'This car is a {self.brand} model {self.model} and it belongs to {self.owner}.'

# Creating an instance of Car
car1 = Car('John Cena', 'Renault', 'Clio', 1200)

car1.modify_engine_size(1600)
car1.modify_owner("Gustavo Larrea")

# Retrieving car state
print(car1.get_info())
