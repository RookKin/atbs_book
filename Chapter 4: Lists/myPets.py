myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = raw_input()
if name not in myPets:
    print('I dont not have a pet named ' + name)
else:
    print(name + ' is my pet.')
