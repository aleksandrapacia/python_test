# test with UNITTEST 
# name test 
from names import get_formatted

print(' Enter "q" to finish the program')

while True:
    first = input('\nEnter your name: ')
    if first == 'q':
        break
    last = input('\nEnter your surname: ')
    if last == 'q':
        break  
    formatted_name = get_formatted(first, last)

    print(f'\tNicely looking name and surname: {first} {last}')

