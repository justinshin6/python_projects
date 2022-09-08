def add_two_numbers(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 + num2}."


def sub_two_numbers(num1, num2):
    return f"The difference of {num1} and {num2} is {num1 - num2}."


def multi_two_numbers(num1, num2):
    return f"The product of {num1} and {num2} is {num1 * num2}."


def div_two_numbers(num1, num2):
    return f"The dividend of {num1} and {num2} is {round(num1 / num2, 2)}."


over = False
while not over:
    user_input = input("Welcome to Justin's Calculator. Type in 'add,' 'subtract,' 'multiply,' " + \
                "or 'divide.' Type in 'quit' to quit the calculator program.")

    if user_input.lower() == 'quit':
        print("Have a good day!")
        over = True
    else:
        if user_input.lower() not in ['add', 'multiply', 'subtract', 'divide']:
            print("Invalid input. Try again")
            continue

        first = int(input("What is the first number? "))
        second = int(input("What is the second number? "))
        if user_input.lower() == 'add':
            print(add_two_numbers(first, second))
        elif user_input.lower() == 'subtract':
            print(sub_two_numbers(first, second))
        elif user_input.lower() == 'multiply':
            print(multi_two_numbers(first, second))
        elif user_input.lower() == 'divide':
            print(div_two_numbers(first, second))












