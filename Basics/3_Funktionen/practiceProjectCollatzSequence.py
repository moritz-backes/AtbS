import sys, time


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = number * 3 + 1
        print(number)
        return number

try:
    while True:
        print("Please enter a number that is an integer.")
        try:
            number = int(input())
            while number != 1:
                number = collatz(number)
        except ValueError:
            print('Please enter an integer, that is a whole number!')
except KeyboardInterrupt:
    print('Thank you for trying this simple program!')
    time.sleep(3)
    sys.exit
