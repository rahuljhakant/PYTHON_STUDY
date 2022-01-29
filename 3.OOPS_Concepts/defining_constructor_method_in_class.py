"""
Defining Constructor method in a class
--------------------------------------

In python, the object creation part is divided into two parts:

Object Creation
Object Initialisation


__new__() method is used to create the object.
__init__() method is used to initialize the object.
__del__() method is used to destroy the object.

"""


class constructor:
    def __new__(self):
        print("New is called when the object is created")

    # def __init__(self, numInt):
    #     self.numInt = numInt
    #     print("object is initialized")

    def __del__(self):
        print("object is destroyed")


obj = constructor();

del obj;
