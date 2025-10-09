"""
- Exercise 10: Call Function using both positional and keyword arguments
- Define a function describe_pet(animal_type, pet_name) that prints a description of a pet.
- Call this function using both positional and keyword arguments.
"""

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"His name is {pet_name}")

describe_pet("dog", "Kuro")
describe_pet(pet_name="Kino", animal_type="cat")