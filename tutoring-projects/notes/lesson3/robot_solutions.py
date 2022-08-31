# 1.) Hurdle One
"""
def turn_right():
    for i in range(3):
        turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(6):
    jump()
"""

# Hurdle Three
"""
def turn_right():
    for i in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
"""

# Hurdle Four

"""
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
"""
