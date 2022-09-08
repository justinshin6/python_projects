"""
Lesson Objectives: Functions, Return Types, Hurdle Challenges
"""

"""
Day 2 Review: In Day 2, we mainly went over everything that had to do with arrays, such as editing and 
manipulating arrays so that we can achieve a certain goal. In order to refresh our memory about arrays,
here is an example exercise that we can do. 
Review Exercise: 
- Create an array of numbers (doesn't matter how many numbers) 
- Use a loop to loop through the array of numbers so that you print out each number in the array
"""

# 1.) Functions
"""
Definition: A function is simply a “chunk” of code that you can use over and over again, rather 
than writing it out multiple times.
- In other words, a function is a block of code that we can use repeatedly so that we can reduce the 
amount of code that we write in total. 
Basic Format of a Function: 
def function_name():
    # body of the function
- The "def" keyword is the keyword that tells the computer that the following code is a function. 
- The function_name is the name of the function that has to be followed by parenthesis(). 
- The body of the function is the indented piece of code where the function information will be stored. 
Example:
def get_name():
    return "Justin"
- This is a simple function that returns my name. 
"""

"""
Definition vs Declaration: 
- Whenever we make a function, that doesn't meant that the function will be run. When we make a function,
we are simply DEFINING the function. We are making the function so that we can use it at a later time. 
- Whenever we DECLARE or CALL a function, that's when the material inside of the function will be run. 
Exercise: Create a function called add_two_numbers() that returns the sum of two numbers of your choice. 
Print out your answer. 
Write your answer below:
"""

"""
Function Exercise: Reeborg Robot Function Calling:
1.) Explore function calling in the following robot environment: 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
2.) Complete the Hurdle 1 Challenge: 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
3.) Complete the Hurdle 3 Challenge: 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
4.) CAPSTONE CHALLENGE: Complete the Hurdle 4 Challenge: 
http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
"""

"""
Function Parameters/Arguments: 
- Parameters: specific inputs that are inserted into a function that we can use for a specific function call.
The parameters will always be inside of the parenthesis beside of the function name separated by commas.
- Argument: the specific information that gets inputed into the function
Example: 
def my_function(fname):
  print(fname)
my_function("Justin")
- In this case, the parameter would be the fname parameter that is inside of the function, and the 
argument would be "Justin" which is the actual information that gets passed into the function.
"""

"""
Function Parameter Exercises: 
1.) What will be the output of the following function? 
def print_email(email):
    print("My email is the following: " + email)
print_email("justinshin6@gmail.com")
2.) What will be the output of the following function? 
def find_remainder(num1, num2):
    return num1 % num2
print(find_remainder(7, 3))
3.) What will be the output of the following function? 
def sum_up_array(arr):
    total = 0
    for n in arr:
        total += n
    return total
print(sum_up_array([1, 2, 3, 4, 5]))
4.) What will be the output of the following function? 
def find_remainder(num1, num2):
    return num1 % num2
print(find_remainder(7, 3, 3))
"""

"""
Type Errors: Type errors occur when there is a difference between the number of parameters and the number of 
arguments that are given in a function. 
"""

"""
CAPSTONE CHALLENGE: Make your own Calculator
Steps:
1.) Create four functions that add, subtract, multiply, and divide two numbers and return the output. 
2.) Use a flag variable and a while loop to get the input from the user
3.) Once the user types in a command, ask for two numbers, and then perform the operation 
4.) If the user doesn't type a correct command, say that the input is invalid and to try again. 
"""

# def get_name(parameter):
#     return parameter
#
# name1 = get_name("Lucy")
# name2 = get_name("Justin")
# print(name1) # Lucy
# print(name2) # Justin

def add(num1, num2):
    return num1 + num2

num1 = add(3, 4)
"""
F-Strings
"""
name = 394875394759034750374503740
print(f"My name is {name}.")
