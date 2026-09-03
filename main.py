import random

lowest_num = 1

highest_num = 100

random_num = random.randint(lowest_num, highest_num)

is_guessed = True

guesses =0

while is_guessed:
    user_guess = input(f"Guess a number between {lowest_num} and {highest_num}: ")
    if  user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1

        if user_guess == random_num:
            print(f"You guessed it! The number was {random_num}.")
            is_guessed = False
        elif user_guess < random_num:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    else:
        print("Please enter a valid number.")

    