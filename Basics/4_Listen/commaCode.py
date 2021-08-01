list = ['apples', 'bananas', 'tofu', 'cats']

def listToString(list):
    if len(list) == 0:
        print('There is nothing in your list.')
    finalString = ''
    for n in range(len(list)):
        if n != len(list) -1:
            finalString += list[n] + ', '
        else:
            finalString += ' and ' + list[n]
    return finalString

print(listToString(list))

