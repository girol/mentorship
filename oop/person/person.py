"""Person Class: Create a class that models a person:

Attributes: name, age, weight and height
Methods: Getting older, gaining weight, losing weight, growing.
 Note: By default, every year our person ages, if their age is less than 21 years old, they must grow 0.5 cm."""


class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_older(self):
        self.age += 1
        if self.age < 21:
            self.grow(1)

    def gain_weight(self, amount):
        self.weight += amount

    def lose_weight(self, amount):
        self.weight -= amount

    def grow(self, cm):
        self.height += cm

    def __str__(self):
        return f"Name: {self.name}, Age:{self.age}, Weight: {self.weight}, Height: {self.height}cm"
