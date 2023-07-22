# alien_0 = {'color':'green','point':20}
# alien_1 = {'color':'red','point':10}
# alien_2 = {'color':'blue','point':5}


# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)
    
    
#make a list of 30 aliens
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
#show the first five alien

for alien in aliens[:5]:
    print(alien)
print('...')


#show how many lines have been created

print(f'The total number of aliens is: {len(aliens)}')

#list in a dictionary
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}

#summarize the order
print(f"you have ordered  a {pizza['crust']}- crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)
    
#a dictionary in a dictionary

users = {
    'jmganga':{
        'first':'jack',
        'last':'mganga',
        'location':'kijitonyama'
    },
    'jmagwaya':{
        'first':'john',
        'last':'magwaya',
        'location':'ubungo'
    },
    'lmike':{
        'first':'leonard',
        'last':'michael',
        'location':'goba'
    }
}


for name,user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}" 
    location = user_info['location']
    print(f'username is {name.title()},')
    print(f'full name is {full_name.title()},')
    print(f'location is {location.title()},\n')
    