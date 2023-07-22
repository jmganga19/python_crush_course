# names = ['jackson','zuhura','abdallah','muhsin']
# print('*******order from first to last*******')
# print(names[0].title())
# print(names[1].title())
# print(names[2].title())
# print(names[3].title())
# print('*******order from last to first*******')
# print(names[-1].title())
# print(names[-2].title())
# print(names[-3].title())
# print(names[-4].title())


# # modifying list
# names[0]= 'juma'
# print(names)
# # add element at the end of list

# names.append('jackson')
# print(names)

# # insert element into list
# names.insert(0,'Anitha')
# print(names)


# # Remove element from the list
# del names[0]
# print(names)


# # remove item using pop method
# popped_name = names.pop()
# print(names)
# print(popped_name)


# # remove item  by value

# names.remove('zuhura')
# print(names)


# Organizing a List
# i) sorting  a list permanently with the sort() method 

cars = ['bmw','gmc','audi','subaru','ist']
cars.sort()
# print(cars)

#  sort in reverse alphabetical order

cars.sort(reverse=True)
# print(cars)


# ii) Sorting list temporary with the sorted() Function
cars = ['bmw','gmc','audi','subaru','ist']
print('Here is the original list:')
print(cars)

cars = ['bmw','gmc','audi','subaru','ist']
sorted_cars = sorted(cars,reverse=True)
print(sorted_cars)

print('Here is the original list again:')
print(cars)

# length of a list
print(len(cars))

