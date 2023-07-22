# prompt = "\nEnter a something and i will print back to you:"
# prompt += "\npress q to quit."
# # here comes flag
# active = True
# message =  ""
# while active:
#     message = input(prompt)
#     if (message =='q' or message =='Q'):
#        active = False
#     else:
#        print(message)
       
#use a break to exit a loop

# prompt = "\nplease enter a place you have visited"
# prompt += "\nEnter quit to quit the program"

# while True:
#    city = input(prompt)
#    if city == 'quit':
#       break
#    else:
#       print(f'my favorite place i visit is{city.title()}')
      
      
      
# continue return top of the loop to skip some execution
print('Odds number between 1 and 10 are:')
current_number = 0
while current_number < 10:
   current_number +=1
   if current_number % 2 == 0:
     continue
   else:
      print(current_number)
