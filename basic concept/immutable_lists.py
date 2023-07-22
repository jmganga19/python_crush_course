# immutable list in python are thos elist which do not change

# tuple are immutable lists in python
dimensions = (10,20)

print(dimensions[0])
print(dimensions[1])


# note tuple with one element are built using one comma
my_t = (2,)
# for loop with tuple
for dimension in dimensions:
    print(dimension)
    
#  equality(==),inequality(!=),greater than (>),less than(<),greater than or equal to(>=),less than or equal to(<=)
# check multiple condition you can use "and"
# for both condition and "or" for one of them
age = 18
sex = 'male'

if(age >= 18 and sex == 'male'):
    print('adult') 
    
    
    
# check wether value is in list


names = ['hello','juma','ommy']
user = 'ommy'
if(user in names):
    print('yes')
    


# check if not in list

user = 'jackson'
if(user not in names):
    print(f'{user} is not in list')

