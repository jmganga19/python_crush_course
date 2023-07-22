pet_0 = {'name':'dog','color':'black','age':3,'owner':'jack'}
pet_1 = {'name':'cat','color':'grey','age':1,'owner':'mimi'}
pet_2 = {'name':'bobi','color':'white','age':1,'owner':'mama'}



pets = []
pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
    print(pet['name'])  
    print(pet['color'])   
    print(pet['age'])  
    print(f"{pet['owner']}\n")   
     
     
