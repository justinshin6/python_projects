class Animal:

    # the constructor of the animal class
    def __init__(self, name, age, color):

        self.name = name
        self.age = age
        self.color = color

    def getName(self):
        """
        Returns the name of the animal
        """
        return self.name

    def getAge(self):
        """
        Returns the age of the animal
        """
        return self.age

    def changeAge(self, diff, add):
        if add:
            self.age += diff
        else:
            self.age -= diff

    def getColor(self):
        return self.color


# Creating Objects of a class
animal1 = Animal("Jeff", 13, "green")
animal2 = Animal("Theodore", 17, "purple")

"""
If we create an object of a class, then we have access to all of the attributes and functions that are inside 
of that class. 
"""
print(animal1.getAge())


"""
Notes for reflection: 
1.) What is def __init__?
- This is something called the constructor of a class. This is a special type of function that gets called whenever you 
create new Objects of a class. The __init__ stands for initialize which pretty much means that this funciton will be 
called first whenever a new object is made. 
2.) What is the self keyword? 
- The self keyword is used to represent an instance (object) of a given class. For example, in order to use methods in 
this class, you have to create an object for the class. Once an object is made, the self keyword attaches itself to that 
specific object. Every function inside of a class needs the self method to be attached to an object.
3.) Well, then how do you create the object?
- In the example above, you can create an object using the following convention: 
animal1 = Animal("name", age)
- In general, you would use the following convention:
object_name = Class_name("parameters")
- As you can see, the object names are in lowercase while the class names are always in lowercase. This is very 
important to distinguish between objects of a class and the class name itself. 
"""

"""
Classes Exercises:
1a.) Create a new object called animal3 whose name is "Zyra" and whose age is 10
1b.) With the animal3 object, increase the age from 10 to 20
1c.) Print out the new age of the animal3 using the getAge() function

2a.) Create a new function inside of the Animal class called changedName that takes in a name as a parameter of the function.
2b.) Set the instance variable of self.name equal to the new changedName parameter.
2c.) Change the name of animal3 from "Zyra" to a name of your choice
2d.) Print out the new name of animal3
"""




