# Use while loop to move items from one list to another
unconfirmed_users = ['jack','jill','kondeboy','jeshi']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
print('The following are users confirmed')
for confirmed_user in confirmed_users:
    print(confirmed_user)
    
# remove all instance of a specified value in list
pets = ['dogs','cat','gorilla','donkey','cat','monkey','rabbit']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)