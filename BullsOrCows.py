import random


def get_digits(number):
    digits = []
    num = int(number)
    for x in range(4):
        last_digit = num % 10
        digits.append(last_digit)
        num = num // 10
    return digits


def check_for_bulls(num_list, guess_list):
    num_of_bulls = 0
    for x in range(len(num_list)):
        if num_list[x] == guess_list[x]:
            num_of_bulls += 1
    return num_of_bulls


def check_for_cows(num_list, guess_list):
    num_of_cows = 0
    for x in range(len(num_list)):
        if num_list[x] == guess_list[x]:
            continue
        for y in range(len(guess_list)):
            if num_list[x] == guess_list[y]:
                num_of_cows += 1
    return num_of_cows


class Game(object):
    attempt_limit = 15
    num_of_attempts = 0
    random_number = random.randrange(1000, 9999)
    num_list = get_digits(random_number)

    print(random_number)

    while num_of_attempts < attempt_limit:

        guess_number = input("What is your guess? ")
        guess_list = get_digits(guess_number)

        num_of_bulls = check_for_bulls(num_list, guess_list)
        num_of_cows = check_for_cows(num_list, guess_list)

        if num_of_bulls == 4:
            print(f"You guessed the number! It took you only {num_of_attempts} attempts, to guess {random_number}")
            break
        else:
            print(f"You got {num_of_bulls} bulls")
            print(f"You got {num_of_cows} cows")

        num_of_attempts += 1

    if num_of_attempts == 15:
        print("You lose!")