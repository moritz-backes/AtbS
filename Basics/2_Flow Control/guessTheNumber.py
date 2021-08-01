# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess. You got ' + str(7 - guessesTaken) + ' chances left.')
    guess = int(input())

    if guess not in range(1, 20):
        print('Can you read? The number is between 1 and 20.')
    elif guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, took you too long. The number I was thinking of was ' + str(secretNumber) + '.')
