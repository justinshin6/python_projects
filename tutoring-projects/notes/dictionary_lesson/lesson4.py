"""
Lesson Objectives: Introduction to Python Dictionaries
"""

"""
Data Structure Overview: 
- Variable: a container that stores a value
Ex: name = "Justin" -> this is a variable that stores the value "Justin"  
- Array: a 'container' of containers that stores variables at certain index positions 
Ex: justin_info = ["Justin", 19, True, "Black"]
- In the array example above, we see that at index position 0, we have my name, at index position 1, we have my age, at
index position 2, we have whether or not I'm having a good day, and at index position 3, we have my hair color. 
- While arrays are good to store values when we want to store things by position, wouldn't it be easier to store these
items in a category -> item type of relationship. For example, we could have the following: 
justin_info = {
    "name": "Justin",
    "age": 19,
    "goodDay": True,
    "HairColor": "Black"
}
"""



"""
The information above is called a Python Dictionary which is the second type of data structure that we will learn. 
- Definition: A python dictionary is a data structure used to store data values in something called key:value pairs. 
- They are written with curly brackets instead of square brackets (that are used in arrays). 
- Definition: The key is the category that is a part of the dictionary. There are no duplicate keys, or in other words,
there cannot be two key values that are the same. Think of a key almost like an "id" for a specific value. 
- Definition: The value of a key is the values that are linked with certain keys in the dictionary. 
Dictionary Exercises:
1.) In the justin_info dictionary above, how many keys are there inside of the dictionary? 
2.) Is it possible for a dictionary to have two of the same keys? 
3.) What is the value for the "goodDay" key inside of the justin_info dictionary? 
4.) Create your own dictionary with your own information below. 
"""

"""
Accessing Values inside of the dictionary: 
- The way to access values inside of a dictionary is the following: Once again, if we had the following dictionary, 
justin_info = {
    "name": "Justin",
    "age": 19,
    "goodDay": True,
    "HairColor": "Black"
}
, then how would we access "Justin" for example? 
- The way this works is that you will just do print(justin_info["name"]). 
- You put the key whose value that you want to access in square brackets right next to name of the dictionary. 
Dictionary Exercises: 
1.) Using justin_info, what will be printed out in the following? 
print(justin_info["HairColor"])
2.) Using justin_info, what will be printed out in the following? 
print(justin_info["key"])
- Hint: This is similar to when we are trying to access an array index that is not possible. 
"""


"""
KeyError: Whenever we are trying to access a value of a key that doesn't exist, a KeyError shows up which tells us that 
they key that we are trying to access does not exist. 
"""

"""
Coding Exercise: Coin Change
- Objective: Use inputs to take in the number of pennies, nickels, dimes, and quarters. After taking in these inputs, 
use a Python dictionary to output the number of coins -> counts. For example, if I have 5 pennies, then I want to 
output "pennies": 5. 
- Additional Challenge: Then, I want you to create a function that returns the total dollar amount that you have with
the amount of coins that you have rounded to two decimal places. 
"""

"""
Coding Exercise: Blind Auction
- Objective: Use inputs to take in a name and a certain bid amount for that person. After taking in these names, whenever
the blind auction is over, return the name with the highest bid amount using a Python dictionary to store a person's 
name to their bid amount. 
- Additional Challenge: Make sure that there are no duplicate names by using an if statement to check to see if a name
is already inside of a dictionary. 
- Hint 1: use a dictionary to store names -> bid amounts 
- Hint 2: You will probably need a function that takes in a dictionary as a parameter that returns the name of the 
highest bidder out of the key-value pairs inside of the dictionary. 
"""

"""
Reflection: All in all, Python dictionaries are another form of data structure that allows us to store elements 
in key-value pairs. It is very useful because we are able to establish relationships between our variables. Therefore, 
the two main data structures that we know now are dictionaries and arrays. 
"""