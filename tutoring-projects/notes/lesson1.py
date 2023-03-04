# Day 1 Python Lesson

"""
Lesson Objectives: Variables, Data Types, Inputs, Conditionals, For/While Loops
Optional: Arrays, Iteration, IndexErrors
"""

# 1.) Variables

# What are the three main types of variables in Python?

"""
Variable Exercises: 
1a.) Create three variables: a variable called 'name' that stores your name, a variable called 'age' that 
stores your age, and a variable called 'happy' that is set to True
1b.) Now, take the age variable that you just created and change it to 0 
1c.) Now, take the age variable that is now set to 0 and increment it by 10 
1d.) Combine the variables into one string to output the following: 
'My name is {name} and I am {age} years old'
"""
"""
2a.) What ouput will be displayed with the following code? 
x = 10
y = 25 
print(x + y)
"""
"""
2b.) If the variables were Strings, what will be displayed with the following code? 
x = '10'
y = '25'
print(x + y)
2c.) How could we change the type of the variables to print out the value that we want? 
"""
"""
3.) What will the following print out? 
a = 5
b = 6
print(a < b)
print(a > b)
print(a == b)
Question: What is the difference between one and two equal signs when it comes to variables? 
"""

# 2.) Inputs

"""
Input Exercise: 
1.) Similar to Variable exercise 1a.), create a variable called age and name; however, store
the values of these variables by using the input function and then print out the values
"""

# 3.) Conditionals

"""
If: 'If this condition is True, then run the code underneath this indent'
Elif: 'If the condition above is NOT True, then run the code underneath this indent'
Else: 'If nothing above is True, then run everything else underneath this indent'
"""
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

"""
Conditional Exercises: 
1.) Combine user input with conditionals. 
- Create a variable called number that is equal to 5. 
- Create another variable called user_input that takes in an input from the user. 
- Now write an if statement that prints out 'YAY' if the user_input is greater than the number, 
prints out 'NO' if the user_input is less than the number, and 'EQUAL' if the user_input is equal to the number
"""

"""
2.) What will the following code output? 
x = 2
print(x)
if x > 3:
    x += 2
    print(x)
"""
"""
3.) What will the following code output? 
x = 2
print(x)
if x > 3:
    x += 2
print(x)
"""

"""
4.) What will the following code output? 
x = 5
if x > 3:
    x += 2
    print(x)
"""
"""
CAPSTONE CHALLENGE 1 : GRADE CALCULATOR
- Using what you know about if, elif, and else statements write a grade calculator that meets the following conditions: 
- Create a variable called grade that stores a input from the user 
- If the grade is greater than or equal to 90, print out 'A'
- If the grade is greater than or equal to 80 but less than 90, print out 'B'
- If the grade is greater than or equal to 70 but less than 80, print out 'C'
- If the grade is lower than 70, print out 'F'
"""

# 4.) Iterations: For/While Loops
# 4a.) For Loops
"""
Definition: For loop is used to check for certain conditions and then
repeatedly runs a block of code as long as those conditions are met.
"""


"""
For Loops Exercises:
1.) What will the following code output? 
for i in range(1, 11):
    print(i)
2.) Print out the numbers 7 - 17 inclusive only 
"""
# 4b.) While Loops

"""
Definition: The while loop is used to repeat a section of code infinite times until a specific condition is broken.
"""

"""
1.) Do the same exercises for the for loop with the while loop 
"""

# 4c.) Modulo
"""
Definition: It returns the remainder of dividing the left hand by right hand 
Ex: 5 % 5 -> 0; 7 % 3 -> 1; 2 % 3 -> 2
"""

"""
Challenge: How could we use Modulo to determine whether a number is an even or odd number? 
"""

"""
CAPSTONE CHALLENGE: Use a while loop or for loop to print out only the even numbers from 1 - 100 inclusive
"""
"""
CAPSTONE CHALLENGE: Guess the Number Project
"""
# We need the user to guess the number
# If blocks -> if the number is too low or if the numbers is too high
""" Steps:
1.) Use a while loop and a flag variable so that when the user guesses the correct number, the game stops
2.) Use if statements, in order to guide the user in the right direction
3.) Implement random numbers
"""



































