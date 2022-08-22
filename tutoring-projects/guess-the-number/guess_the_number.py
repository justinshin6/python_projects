import random


def regular_guess_the_number():
    """
    Regular guess the number game with no additional constraints
    """
    random_number = random.randint(1, 100)
    user_input = int(input("Please put in a number from 1-100 "))
    while random_number != user_input:
        if user_input > random_number:
            print("That guess is too high. Try again with a lower number.")
            user_input = int(input("Please put in a number from 1-100 "))

        elif user_input < random_number:
            print("That guess is too low. Try again with a higher number.")
            user_input = int(input("Please put in a number from 1-100 "))
    print("That's right")

regular_guess_the_number()

def advanced_guess_the_number():
    """
    - Use a variable to track how many guesses the user has made already.
    - When they win, tell them how many tries it took.
    - Let your user set the upper bound or choose a difficulty mode.
    - Maybe instead of guessing a number between 1 and 100, they have to guess between 1 and 1000!
    - In addition to generating a random number that the user is trying to guess,
    - generate a second random trapped number that the user is trying to avoid.
    - If the user guesses the death number, it's game over!
    """


    upper = int(input("Please enter an upper bound. "))
    while upper < 2:
        print("Invalid input. Try again.")
        upper = int(input("Please enter an upper bound. "))
    guess_tracker = 1

    # generating target number
    target_number = random.randint(1, upper)
    print("Target " + str(target_number))
    # generating death number
    death_number = random.randint(1, upper)

    # Edge Case: if death number equals target number
    while death_number == target_number:
        death_number = random.randint(1, upper)
    print("Death " + str(death_number))

    user_input = int(input("Please put in a number from 1-" + str(upper) + " "))
    while user_input < 1 or user_input > upper:
        print("Invalid input. Try again.")
        user_input = int(input("Please put in a number from 1-" + str(upper) + " "))
    
    # actual checking the function
    while target_number != user_input and user_input != death_number:
        if user_input > target_number and user_input != death_number:
            print("That guess is too high. Try again with a lower number.")
            if user_input > death_number:
                print("That's higher than the death number.")
            else:
                print("That's lower than the death number.")
            user_input = int(input("Please put in a number from 1-" + str(upper) + " "))
            while user_input < 1 or user_input > upper:
                print("Invalid input. Try again.")
                user_input = int(input("Please put in a number from 1-" + str(upper) + " "))
            guess_tracker += 1

        elif user_input < target_number and user_input != death_number:
            print("That guess is too low. Try again with a higher number.")
            if user_input > death_number:
                print("That's higher than the death number.")
            else:
                print("That's lower than the death number.")
            user_input = int(input("Please put in a number from 1-" + str(upper) + " "))
            while user_input < 1 or user_input > upper:
                print("Invalid input. Try again.")
                user_input = int(input("Please put in a number from 1-" + str(upper) + " "))
            guess_tracker += 1

    if target_number == user_input:
        if guess_tracker != 1:
            print("You're right. You got the answer in " + str(guess_tracker) + " guesses.")
        else:
            print("You're right. You got the answer in one guess.")
    if death_number == user_input:
        if guess_tracker != 1:
            print("Oh no. You hit the death number. You have made " + str(guess_tracker) + " guesses.")
        else:
            print("Oh no. You hit the death number on the first try")
    repeat_answer = input("Play again? (Y/N) ")
    if repeat_answer.lower() == "y":
        advanced_guess_the_number()
    elif repeat_answer.lower() == "n":
        print("Thank you for playing!")
    else:
        print("Invalid answer!")


# Function Calls
# advanced_guess_the_number()






