import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

is_running = True

guess = lowest_num - 1
guesses = 0
max_guesses = 7


while is_running:
    guess = input(f'Guess a number between {lowest_num} and {highest_num}: ')
    is_running = guesses <= max_guesses

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f'Guess a number between {lowest_num} and {highest_num}: ')

        if guess < answer:
            print('Your answer is too low')
        elif guess > answer:
            print('Your answer is too high')
        else:
            print('You guessed the correct number!')
            break
    else:
        print('Invalid input')
        print(f'Guess a number between {lowest_num} and {highest_num}: ')