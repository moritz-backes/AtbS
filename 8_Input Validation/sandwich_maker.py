import pyinputplus as pyip

def sandwich_maker():
    bread_type = bread_chooser()
    protein_type = protein_chooser()
    cheese_type = cheese_chooser()
    additions = addition_chooser()
    how_many = how_many_chooser()

    if how_many == 1:
        print(f'You chose to get {how_many} sandwich with {bread_type} bread, {protein_type}, {cheese_type} and {additions}.')
    else:
        print(f'You chose to get {how_many} sandwiches with {bread_type} bread, {protein_type}, {cheese_type} and {additions}.')

def bread_chooser():
    prompt = 'What kind of bread would you like for your sandwich?\n'
    bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt, numbered=True)
    return bread_type

def protein_chooser():
    prompt = 'What kind of protein source yould you like on your sandwich?\n'
    protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt, numbered=True)
    return protein_type

def cheese_chooser():
    prompt1 = 'Would you like cheese on your sandwich?\nPlease answer yes or no.\n'
    answer1 = pyip.inputYesNo(prompt1)
    if answer1 == 'yes':
        prompt2 = 'What kind of cheese would you like on your sandwich?\n'
        cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt2, numbered=True)
        return cheese_type
    else:
        cheese_type = 'no cheese'
        return cheese_type

def addition_chooser():
    prompt = 'Would you like mayo, mustard, lettuce or tomato on your sandwich?\nPlease answer yes or no.\n'
    answer = pyip.inputYesNo(prompt)
    if answer == 'yes':
        additions = 'mayo, mustard, lettuce and tomato'
        return additions
    else:
        additions = 'no additions'
        return additions

def how_many_chooser():
    prompt = 'How many sandwiches would you like?\n'
    how_many = pyip.inputInt(prompt, min=1)
    return how_many

sandwich_maker()
