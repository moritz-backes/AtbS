#! python3
# date_detection.py - This program finds dates in the format DD/MM/YYYY and checks if they are a valid date

import re

def date_finder_function(text):
    date_finder = re.compile(r'''(
        (0[0-9]|[12][0-9]|3[01])
        /
        (0[0-9]|1[012])
        /
        ((?:19|20)\d\d)
        )''', re.VERBOSE)

    dates = date_finder.search(text)
    return dates.group(2, 3, 4)

#check if leap year
def leap_year_checker(year):
    if int(year) % 4 == 0:
        if int(year) % 100 != 0 or int(year) % 400 == 0:
            #print('It is a leap year!')
            return True
    #print('Not a leap year')
    return False

#check days in month, if leap year special condition for february
#31: January, March, May, July, August, October, December
#30: April, June, September, November
#28-29: February

def day_checker():
    day, month, year = date_finder_function(text)
    _31_days_list = [1, 3, 5, 7, 8, 10, 12]
    _30_days_list = [4, 6, 9, 11]
    if int(month) in _31_days_list and int(day) in range(1, 32):
        print('This is a correct date.')
    if int(month) in _30_days_list and int(day) in range(1, 31):
        print('This is a correct date.')
    if int(month) == 2:
        if int(day) in range(1, 29) and leap_year_checker(year) != True:
            print('This is a correct date.')
        if int(day) in range(1, 30) and leap_year_checker(year) == True:
            print('This is a correct date.')
        else:
            print('This is not a correct date.')
    else:
        print('This is not a correct date.')

#print('Please enter a date in the format dd/mm/yyyy so we may verify it for validity')
text = '29/02/1928'
day_checker()
