"""
    Constructor is a special type of function that is called automatically whenever an object of that class is created
"""


"""
In Python the __init__() method is called the constructor and is always called when an object is created.
"""


class Happy:

    def __new__(self):
        print("New called when the object is created")

    def __init__(self):
        print("Happy Birthday")


obj = Happy()
# By writing  Happy() in the code above, we are informing python that obj is an object of
# class Happy and that is exactly when the constructor of that class is called.

# Constructors are used to initialize the variables of the class for an object(instance),
# although it can perform some other tasks as well, like checking if there are enough resources,
# if the value used to initialize any variable is valid or not, etc.


# Defining Constructor method in a class

class Example:
    myVariable = "some value"

#  here we are explicitly defining the constructor method for the class Example and changing its return type to String.
    def __new__(self):
        return 'studytonight'


# creating object of the class Example
mutantObj = Example()

# but this will return that our object
# is of type str
print(type(mutantObj))
