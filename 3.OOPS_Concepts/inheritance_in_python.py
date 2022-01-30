# Parent class
class Parent:
    # class variable
    a = 10
    b = 100
    # some class methods

    def doThis(self):
        print("Doing this")

    def doThat(self):
        print("Doing that")

# Child class inheriting Parent class


class Child(Parent):
    # child class variable
    x = 1000
    y = -1
    # some child class method

    def doWhat(self):
        print("Doing what")

    def doNotDoThat(self):
        print("Doing not that")


parentObj = Parent()

childObj = Child()

# Illegal
# parentObj.doWhat()

# legal
childObj.doThis()
print(childObj.a)
print(childObj.b)

"""Benefits of using Inheritance in Python
    * code reusability
    * code maintainability
    * Structured Code
"""


# Python - Multiple Inheritance
# Python - Multilevel Inheritance


# Using issubclass() method
class Parent:
    var1 = 1

    def func1(self):
        print("Doing something in parent")


class Child(Parent):
    var2 = 2

    def func2(self):
        print("Doing something in child")


print(issubclass(Child, Parent))
