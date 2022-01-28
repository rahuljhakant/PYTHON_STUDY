import math
from time import process_time
from xmlrpc.client import boolean

from pkg_resources import PEP440Warning
print('Hello world program!!')
print('Hello rahul, How are you?')

"""
Numbers in python

"""

print('addition ', 1+1)
print('substraction ', 2-2)
print('multiple', 3*2)
print('Division', 44/2)
print('Modulus', 10 % 5)
print('Power', 2 ** 3)

"""
Math Functions in Python

"""

print('Pow', pow(10, 2))
print('Absolute', abs(-99.888))
print('Sine ', math.cos(120))
print('Floor division  ', 12.5//4)

"""
Comparison Operators in Python

"""

print('== ', 2 == 2)
print('!= ', 3 != 4)
print('>  ', 2 > 1)


"""
Logical Operators in Python

"""


if 3 > 1 and 3 > 2:
    print('and operator')


if 4 > 2 or 3 > 1:
    print('or  operator')


x = 20
if not x > 20:
    print('not in python')


"""
Membership Operators in Python

"""

if 'i' in 'String':
    print('in in python')

if 'i' not in 'Apple':
    print('not in in python')

"""

Identity Operators in Python

"""

if (2 > 1) is True:
    print('is true')

if (1 > 10) is not True:
    print('is not true')


# x = input('Enter the number')
# print(int(x) ** 2)


"""
  Data types in Python
  --------------------
1. Numbers
2. None
3. Sequences
4. Sets
5. Mappings

"""

"""[Number]
"""
a = 10
b = 200

"""[None]
"""
c = None

"""[Sequence]
    Strings
    List
    Tuple
    Sets
"""

hello = "Hello"
Hello_List = [1, 2, 3, "hello", "List"]
hello_Tuple = (1, 2, 3, "hello", "list")
hello_Set = {1, 2, 4, 4, 4}

print(type(hello))
print(type(Hello_List))
print(type(hello_Tuple))
print(type(hello_Set))
print(hello_Set)

"""[Mapping]
             Dictionaries : here data type is stored in key value pair.
"""

Dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(type(Dict))
print(Dict)


