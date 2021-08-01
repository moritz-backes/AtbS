import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    # pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    promt = f'{question_number}: {num1} x {num2} = '
    try:
        # right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(promt, allowRegexes=[f'^{num1 * num2}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # this block runs if no exceptions were raised in the try block
        print('Correct!')
        correct_answers += 1
    time.sleep(1) # brief pause to let the user see the result

print(f'Score: {correct_answers / number_of_questions * 100}')
