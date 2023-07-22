usernames = []  # this check if list is empty
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username},would you like to see status report?')
        else:
            print(f'Hello {username},thank you for logging in again')
else:
    print('Weneed to find some users!')