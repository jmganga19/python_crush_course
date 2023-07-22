#position arguments---> this match arguments in function call 
# with the  parameter in function definition
#note order matter in position parameters


def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster','harry')
describe_pet('dog','bruce')


#Keyword arguments----> it is a name-value pair that you pass to a function

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='cat',pet_name='pussy')
describe_pet(pet_name='bobi',animal_type='dog')

#default values  for each parameter

def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")