# age = 4
# if age < 2:
#     print('you are a baby')
# elif age >=2 and age < 4:
#     print('you are a toddler')
# elif age >=4 and age < 13:
#     print('you are a kid')
# elif age >=13 and age < 20:
#     print('you are a teenager')
# elif age >=20 and age < 65:
#     print('you are a adult')
# else:
#     print('you are elder')

# print('#########Excercise#########')
# alien_color = 'red'
# if alien_color == 'green':
#     print('you have any 5 points')
# elif alien_color == 'yellow':
#     print('you have just earn 10 points')
# elif alien_color == 'red':
#     print('you have just earn 15 points')
    
    
favorite_fruits = ['Banana','Mango','Apple','Avocadro']

# # make sure to follow exactly what is in list
# if 'banana'.title() in favorite_fruits:
#     print('You really like banana')
# if 'mango'.title() in favorite_fruits:
#     print('You really like mango')
# if 'apple'.title() in favorite_fruits:
#     print('You really like apple')
# if 'avocadro'.title() in favorite_fruits:
#     print('You really like avocadro')
    
# using loop and if


for favorite_fruit in favorite_fruits:
    if favorite_fruit == 'apple'.title():
         print('You really like apple')
    else:
        print('Note found')
print('End of the loop')