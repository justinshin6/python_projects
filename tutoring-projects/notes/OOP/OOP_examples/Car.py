class Car:
    def __init__(self, name, color, make, speed):
        self.name = name
        self.color = color
        self.make = make
        self.speed = speed

    # Function that increases the speed of a car by the increment
    def increase_speed(self, increment):
        self.speed += increment

    # Function that compares speed of a car and another car
    def compares_speed(self, car1):
        if car1.speed > car2.speed:
            return f"Car {self.name}'s speed is greater than Car {car1.name}"
        elif car2.speed > car1.speed:
            return f"Car {car1.name}'s speed is greater than Car {self.name}"
        else:
            return "The speed of the two cars were the same."


car1 = Car("Justin", "Red", "Toyota", 60)
car2 = Car("Albert", "Blue", "Tesla", 60)
print(car1.compares_speed(car2))