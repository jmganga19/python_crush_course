person = {
    'first_name':'jakson',
    'last_name':'mganga',
    'age':23,
    'city':'Dar es salaam'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


# using for loop
#1 looping through the keys and value
for key,value in  person.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")
    
#1 looping through all keys 
fav_language = {
    'jack':'C#',
    'john':'python',
    'jill':'dart',
    'mike':'html',
    'zuu':'dart',
    'ommy':'C++',
    'juma':'C++'
}
friends = ['john','mike']
for name in fav_language.keys():
    print(name.title())
    if name in friends:
        language = fav_language[name].title()
        print(f'\tHello {name},i see you love {language}')
        

#check if element is not in dictionary

if 'erick' not in  fav_language.keys():
    print('Erick is not in dictionary.')
    
    
#loop through the particular order


for name in sorted(fav_language.keys()):
    print(f'{name},this is ordered')
    
#looping through all value in dictionary
print('\nthis select value from dictionary with repetation')

for language in fav_language.values():
    print(language)
    
#from the above you can use the word "set" to make the value unique
print('\nthis select value from dictionary without repetation')
for language in set(fav_language.values()):
    print(language.title())