from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
Step 1.) Create Objects of the Menu, MoneyMachine, and CoffeeMaker
Step 2.) Set up a while loop that calls the get_items() function from the 
menu class 
Step 3.) Create an input that says "What would you like" and then prints out the options that are 
available to the user. 
Step 4.) If the choice is "off" then turn off the machine. If the choice is "report" then call report() function 
from the coffee maker and the money_machine
Step 5.) If neither of the options pass above, then call find_drink with the user's choice from the menu class. 
Step 6.) Use an if statement to check if the coffee maker has enough resources and if the money machine can make 
the payment. If both of these things are true, then call the make_drink() method from the coffe_maker class. 
"""