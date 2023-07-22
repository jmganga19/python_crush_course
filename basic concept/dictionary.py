# dictionary is collection of key value pairs.
# you can use key to get value.

alien_0 = {'color':'green','points':5}
print(alien_0)
print(alien_0['color'])

# adding new value to  dictionary
alien_0['x-position'] = 0
alien_0['y-position'] = 25

print(alien_0)

# to remove element in dictionary use delete
# all it need is the name of the dictionary along with the  key

del alien_0['x-position']
print(alien_0)


favorite_languages = {
    'jen':'python',
    'jack':'C#',
    'ommy':'java',
    'mwaj':'C++',
}

print(f"jack favorite language is {favorite_languages['jack']}")


# also you can use get fucntion  to retrive value from the dictionary
# if the value is not assigned you can  have default value
xvalue = alien_0.get('x-position','No points assigned')
print(xvalue)