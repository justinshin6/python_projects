pennies = int(input("How many pennies do you have? "))
nickels = int(input("How many nickels do you have? "))
dimes = int(input("How many dimes do you have? "))
quarters = int(input("How many quarters do you have? "))

coins = {
    "pennies": pennies,
    "nickels": nickels,
    "dimes": dimes,
    "quarters": quarters,

}

def calculate_total():
    return round(pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25, 2)


print("This is how many coins that I have!")
print(coins)
print(f"My total is ${calculate_total()}")








