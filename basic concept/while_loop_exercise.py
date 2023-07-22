print('************A program for a movie theatre************')
prompt = "\n Enter your age"
prompt += "\n Enter q to quit"

while True:
    age = input(prompt)
    if age == 'q':
        break
    elif age < '3':
        print('Congatulation!!,you have free entry.')
    elif age >= '3' and age <= '12':
        print('Ticket price is $10')
    elif age > '12':
        print('Ticket is $12')
    else:
        print('Please enter a valid prompt')
    
        