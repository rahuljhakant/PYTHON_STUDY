"""
Access modifiers are used to limit the access to the variables and functions of a class.

There are three access modifiers:

public: accessible from anywhere.
private: accessible only within the class.
protected: accessible within the class and subclasses.

"""


class modifiers:
    def __init__(self):
        self.public_var = "Public"
        self.__private_var = "Private"
        self.__protected_var = "Protected"

    def public_method(self):
        print(self.public_var)

    def private_method(self):
        print(self.__private_var)

    def protected_method(self):
        print(self.__protected_var)


obj = modifiers()


# public Access Modifier

# defining a class Employee, here all the classes are by default public in nature
class Employee:
    # constructor
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal


# protected Access Modifier adding a prefix _(single underscore) to a variable name makes it protected.
# defining a class Employee

class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name   # protected attribute
        self._sal = sal     # protected attribute

# private Access Modifier adding two underscores to a variable name makes it private.
# While the addition of prefix __(double underscore) results in a member variable or function becoming private.

# defining class Employee


class Employee:
    def __init__(self, name, sal):
        self.__name = name    # private attribute
        self.__sal = sal      # private attribute
