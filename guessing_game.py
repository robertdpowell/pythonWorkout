import random

def guessing_game():
    random_num = random.randint(0, 50)
    guesses = 0

    while guesses < 5:
        user_guess = int(input('guess the number between 1 and 50!\n'))
        guesses = guesses + 1

        if user_guess > random_num:
            print(f'Too high! guesses left --> { 5 - guesses}')

        if user_guess < random_num:
            print(f'Too low! guesses left --> { 5 - guesses}')

        if user_guess == random_num:
            break

    if user_guess == random_num:
        print(f'You got it!! The answer was {random_num}. \nWell done Emilia!')
    else:
        print(f'\n\ngame over Emilia! the number was {random_num}')

if __name__ == '__main__':
    guessing_game()