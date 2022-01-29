# Defining a class is simple, all you have to do is use the keyword class followed by the
# name that you want to give your class, and then a colon symbol :
class Apollo:
    # define a variable
    destination = "moon"

    # definig the member functions
    def fly(self):
        print("Spaceship flying...")

    def get_destination(self):
        print("Destination is: " + self.destination)


obj = Apollo()
obj.fly()
obj.get_destination()
obj.destination = "earth"

"""[About objects]
    # Objects are created when you create a class.
    # Objects are instances of a class.
    # Objects have attributes.
    # Objects have methods.
    # Objects can be created using the class name.
    # Objects can be created using the class name and passing arguments to the constructor.

    1. We add the self parameter when we define a member function, but do not specify it while calling the function.
    2. When we called get_destination function for objFirst it gave output as Destination is: mars, because we updated the value for the variable 
    destination for the object objFirst.
    3. To access a member function or a member variable using an object, we use a dot . symbol.
    4. And to create an object of any class, we have to call the function with same name as of the class.
    5. To call a member function of an object, we use the object name followed by a dot . and the member function name.
    
"""
