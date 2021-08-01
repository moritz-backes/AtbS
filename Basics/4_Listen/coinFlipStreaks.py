import random

#FIXED VAKUES
print('Please enter the number of experiments you wish to conduct!')
NUM_EXPERIMENTS = int(input())
print('Please enter the number of cointosses per experiment!')
NUM_COINFLIPS = int(input())
print('Please enter the length of the streak for which we will check!')
STREAK_LEN = int(input())

#Create list and string with 100 random values for head or tails
def random_list_generator(NUM_COINFLIPS):
    random_list = []
    for _ in range(NUM_COINFLIPS):
        if random.randint(0, 1) == 0:
            random_list.append('H')
        else:
            random_list.append('T')
    return random_list

#Code that checks if there is a streak of 6 heads or tails in a row.
def streak_checker(STREAK_LEN):
    random_string = ''.join(random_list_generator(NUM_COINFLIPS))
    if random_string.count('H' * STREAK_LEN) or random_string.count('T' * STREAK_LEN):
        return True


def repeated_coin_toss_experiment(NUM_EXPERIMENTS, NUM_COINFLIPS, STREAK_LEN):
    successes = 0
    for _ in range(NUM_EXPERIMENTS):
        if streak_checker(STREAK_LEN):
            successes += 1

    print(f"Chance of streak: {successes/NUM_EXPERIMENTS*100:.2f}%")

repeated_coin_toss_experiment(NUM_EXPERIMENTS, NUM_COINFLIPS, STREAK_LEN)
