major_rivers = {
    'rufiji':'Tanzania',
    'nile':'Egypt',
    'congo':'Drc'
}

for river,country in major_rivers.items():
    print(f'The {river.title()} runs through {country.title()}\n')
    
for river in major_rivers.keys():
    print(f'{river.title()} ')
    
for country in major_rivers.values():
    print(f'{country.title()}\n')