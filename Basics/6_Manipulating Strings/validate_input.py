def age_and_password():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')

    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')
    return age, password

user_age, user_password = age_and_password()
print(f'Your age is {user_age} and your password is {user_password}.')
