magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick")
    print(f"I can't wait to see your nrxt trick,{magician.title()}.\n")
print("Thank you,everyone.That was a great magic show!")


# List of numbers

for value in range(1,6):
    print(value)
    

for value in range(6):
    print(value)
    
# convert into list

numbers = list(range(1,6))
print(numbers)

# use the range() function to tell python to skip numbers in a range
even_numbers = list(range(2,10,2))
print(even_numbers)

# concatinate list
result = numbers + even_numbers
print(result)



squares = []
for square in range(2,10):
    value = square**2
    squares.append(value)
    
    
print(squares)
print(sum(squares))
print(min(squares))
print(max(squares))



# list  comprehensions

list_of_numbers = [value**2 for value in range(1,11)]
print(list_of_numbers)