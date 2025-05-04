# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self):
        print(f"{self._name} is being fed!")

    def get_name(self):
        return self._name

    def get_species(self):
        return self.__class__.__name__


# Subclasses
class Cow(Animal):
    def make_sound(self):
        print(f"{self._name} says Moo!")

    def milk(self):
        print(f"{self._name} has been milked.")
        return "Milk"


class Chicken(Animal):
    def make_sound(self):
        print(f"{self._name} says Cluck!")

    def lay_egg(self):
        print(f"{self._name} laid an egg.")
        return "Egg"


class Sheep(Animal):
    def make_sound(self):
        print(f"{self._name} says Baa!")

    def shear(self):
        print(f"{self._name} has been sheared.")
        return "Wool"


# FarmStructure class
class FarmStructure:
    def __init__(self, name: str, structure_type: str):
        self.name = name
        self.structure_type = structure_type

    def describe(self):
        print(f"{self.name} ({self.structure_type})")


# Farm class
class Farm:
    def __init__(self, name="The Belval Farm"):
        self._name = name
        self._animals = []
        self._structures = []

    def add_animal(self, animal: Animal):
        self._animals.append(animal)

    def remove_animal(self, animal: Animal):
        self._animals.remove(animal)

    def add_structure(self, structure: FarmStructure):
        self._structures.append(structure)

    def remove_structure(self, structure: FarmStructure):
        self._structures.remove(structure)

    def show_population(self):
        print(f"Welcome to {self._name}!\nFarm Population:")
        species_count = {}
        for animal in self._animals:
            species = animal.get_species()
            if species in species_count:
                species_count[species] += 1
            else:
                species_count[species] = 1
        for species, count in species_count.items():
            print(f"- {species}: {count}")

    def list_structures(self):
        print("Structures:")
        for structure in self._structures:
            structure.describe()

    def daily_routine(self):
     print("----- Morning Routine ------")
     products_collected = {"Milk": False, "Egg": False, "Wool": False}

     for animal in self._animals:
         animal.feed()
         animal.make_sound()

         if isinstance(animal, Cow) and not products_collected["Milk"]:
             animal.milk()
             products_collected["Milk"] = True
         elif isinstance(animal, Chicken) and not products_collected["Egg"]:
             animal.lay_egg()
             products_collected["Egg"] = True
         elif isinstance(animal, Sheep) and not products_collected["Wool"]:
             animal.shear()
             products_collected["Wool"] = True

     collected = [product for product, collected in products_collected.items() if collected]
     print("Collected products:", ", ".join(collected))




if __name__ == "__main__":
    # Create farm
    my_farm = Farm()

    # Add animals
    my_farm.add_animal(Cow("Bessie", 4))
    my_farm.add_animal(Cow("MooMoo", 5))
    my_farm.add_animal(Chicken("Clucker", 2))
    my_farm.add_animal(Chicken("Feathers", 1))
    my_farm.add_animal(Chicken("Nugget", 3))
    my_farm.add_animal(Sheep("Woolly", 3))
    my_farm.add_animal(Sheep("Fluffy", 4))
    my_farm.add_animal(Sheep("Lamby", 2))
    my_farm.add_animal(Sheep("Sheepo", 5))
    my_farm.add_animal(Sheep("Snow", 3))

    # Add structures
    my_farm.add_structure(FarmStructure("Red Barn", "Barn"))
    my_farm.add_structure(FarmStructure("Hen Palace", "Coop"))

    # Show population
    my_farm.show_population()
    print()
    # List structures
    my_farm.list_structures()
    print()
    # Run daily routine
    my_farm.daily_routine()
