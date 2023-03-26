# Turtle Race Python Project Starting Code

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who win the race? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x = -230, y = y_positions[i])
    all_turtles.append(t)
if user_bet:
    is_race_on = True
while is_race_on:
    for i in range(6):
        turtle = all_turtles[i]
        if turtle.xcor() > 230:
            is_race_on = False

        turtle.forward(random.randint(0, 10))



"""
Step 1: Make Six turtles
- First, you want to use a for loop. How many times should we loop through this for loop? 
- For each index, we need to create a new turtle, pick a color from the colors array, and a y position from the y_positions array.
How can we use our index in order to do this? 
- Use the goto method in order to set the turtle to the right y_position. Set the x position to -230. 
- Add the turtle to the all_turtles array
Step 2: Check if there is a user bet
- Check to see if there is a user bet with an if statement. If it is, then set is_race_on to True. 
Step 3: Main while loop functionality 
- Loop through each turtle in the all_turtles array
- Then after all this, make each turtle move a random amount from (0, 10). How can we use random.randint in order to do this? 
- For each turtle, if the turtle's .xcor() is greater than 230, then they have won the race. 
- Which variable should we change to false? 
- Check to see if the winning color is equal to the user bet by using turtle.pencolor()
- Outside the while loop, call screen.exitonclick()
"""
screen.exitonclick()