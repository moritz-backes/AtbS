myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is one of my pets.')
