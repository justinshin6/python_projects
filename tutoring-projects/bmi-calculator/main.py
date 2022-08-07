"""
BMI-Calculator that calculates the BMI when given the height and the weight 
of a person using the following formulas: 

BMI = kg/(m^2)
- If your BMI is less than 18.5 -> underweight
- If your BMI is 18.5 to 24.9 -> healthy
- If your BMI is 25.0 to 29.9 -> overweight
- If your BMi is 30.0 or higher -> Obese
"""

print("Welcome to the BMI Calculator")
meters = float(input("Enter your height in meters: "))
kg = float(input("Enter your weight in kilograms: "))

bmi = round(kg / (meters ** 2), 2)
if bmi >= 30.0:
    print(f"BMI {bmi}: -> Obese")
elif 30.0 > bmi >= 25.0:
    print(f"BMI {bmi}: -> Overweight")
elif 25 > bmi >= 18.5:
    print(f"BMI {bmi}: -> Healthy")
else:
    print(f"BMI {bmi}: -> Underweight")
