# Day 2 Python Lesson

"""
Lesson Objectives: Arrays, Randomization, Indexing, IndexErrors
Optional: Guess the Number Capstone Challenge
"""

"""
Day 1 Overview: FizzBuzz Job Interview Question
Overview: The FizzBuzz interview question is a very popular computer science question 
asked in interviews. The question is meant to test your ability in looping and modulo which 
are topics that we went over in the previous day. 
Problem Description: Write a program that prints the numbers from 1 to 100 and for multiples of ‘3’ print “Fizz” 
instead of the number and for the multiples of ‘5’ print “Buzz." If a number is a multiple of both '3' and '5', then 
print out "FizzBuzz."
"""

# 1.) Arrays
"""
Definition: Arrays are used to store multiple values in one single variable.
Example:
cars = ["Ford", "Volvo", "BMW"]
Basic Format:
array_name = [value1, value2, ..., valueX]
Exercise:
1.) Create an array called information that contains your age, name, and favorite food.
Write your answer below:
"""

"""
Length of the array: We can use the len() function to return the length of the array
Exercise: 
1.) What will be outputed below? 
cars = ["Ford", "Volvo", "BMW"]
print(len(cars))
2.) What will be outputed below? 
array = []
print(len(array))
"""

"""
Accessing Elements in an array: You refer to an array element by referring to the index number.
Defintiion: the index position of an element is the position in the array where the element is located
- You can access elements by the index position by placing brackets next to the array name and inputting the
index number inside of the brackets. 
Exercise: 
1.) What will be outputed below? 
cars = ["Ford", "Volvo", "BMW"]
print(cars[0])
2.) What will be outputed below? 
cars = ["Ford", "Volvo", "BMW"]
print(cars[3])
"""

"""
Index Errors: An IndexError is an exception in Python that occurs when we try to access an element from an array
from an index that is not present in the list.
Exercises:
1.) Will the following code have an IndexError or not? 
foods = ["pizza", "bananas", "apples", "sushi", "cucumber"]
print(foods[0])
print(foods[2])
print(foods[4])
2.) Will the followint code have an IndexError or not? 
foods = ["pizza", "bananas", "apples", "sushi", "cucumber"]
print(foods[7])
print(foods[6])
print(foods[5])
"""


"""
Editing Arrays:
a.) append(): the append function allows you to add elements to the end of the array 
b.) remove(): the remove function allows you to remove a specific element in the array
c.) Index Position: You can modify an index position by reassigning a value to that 
specific index position 
Exercises:
1.) What will be outputed below? 
hp_chars = ["Harry Potter", "Ron", "Hermione", "Dumbledore"]
hp_chars.append("Professor Snape")
hp_chars.remove("Ron")
print(hp_chars)
2.) What will be outputed below? 
numbers = []
print(numbers)
numbers.append(4)
numbers.append(3)
numbers.append(2)
numbers.append(1)
print(numbers)
3.) What will be outputed below?
numbers = [1, 2, 3, 4, 5]
numbers[2] = 10
numbers[3] = 3
print(numbers)
"""


"""
Looping through arrays: 
a.) For in loop: You can use a for in loop to loop through the elements in the array
Example: 
books = ["Percy Jackson", "Harry Potter", "Magic Tree House"]
for book in books:
    print(book)
Basic Format:
for variable in array:
    # do something 
b.) While loop: You can have an index counter that loops through the elements in the array: 
books = ["Percy Jackson", "Harry Potter", "Magic Tree House"]
index = 0
while index < len(books):
    print(books[index])
    index += 1
"""

"""
CAPSTONE CHALLENGES: These challenges will test your knowledge of arrays, indexing, and 
looping through arrays. 
Challenge 1: Sum of an Array
Objective: Given an array of random numbers, use a loop to print out the sum of the numbers in the array
Answer: You should print out 577 as the final answer.
scores = [87, 69, 45, 90, 100, 31, 60, 95]


Challenge 2: Average of an Array
Objective: Given an array of random numbers, use a loop to find the average of the numbers in the array
Answer: You should print out 72.125 as the final answer.
scores = [87, 69, 45, 90, 100, 31, 60, 95]
Challenge 3: High Score in Array
Objective: Given an array of high_scores, use a loop to print out the highest score in the array
Answer: You should print out 339 as the final answer.
high_scores = [87, 25, 339, 57, 17, 99, 100, 1, 3, 56, 37, 87]
"""