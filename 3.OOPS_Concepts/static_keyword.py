# Static Variables and Methods in Python

# Static Methods in Python

# static methods are the methods which are bound to the class rather than an object of the class and hence are
# called using the class name and not the objects of the class.


class Shape:

    @staticmethod
    def info(msg):
        # show custom message
        print(msg)
        print("This class is used for representing different shapes.")


Shape.info("Welcome to Shape class")

"""
    Following are some important take aways:
    _______________________________________

    1. Static variable and methods are used when we want to define some behaviour or property specific to the class and which is something common for all the class objects.
    2. If you look closely, for a static method we don't provide the argument self because static methods don't operate on objects.
"""
