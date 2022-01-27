import math
from time import process_time
from xmlrpc.client import boolean

from pkg_resources import PEP440Warning
print('Hello world program!!')
print('Hello rahul, How are you?')

print('__________________________________________________________________')
print('\n')
print('*** Numbers in python  ***')
print('\n')

print('addition ', 1+1)
print('substraction ', 2-2)
print('multiple', 3*2)
print('Division', 44/2)
print('Modulus', 10 % 5)
print('Power', 2 ** 3)

print('\n')

print('________________________________________________________________')
print('\n')
print('*** Math Functions in Python ***')
print('\n')

print('Pow', pow(10, 2))
print('Absolute', abs(-99.888))
print('Sine ', math.cos(120))
print('Floor division  ', 12.5//4)

print('\n')

print('________________________________________________________________')
print('\n')
print('*** Comparison Operators in Python ***')
print('\n')
print('== ', 2 == 2)
print('!= ', 3 != 4)
print('>  ', 2 > 1)


print('\n')

print('________________________________________________________________')
print('\n')
print('*** Logical Operators in Python ***')
print('\n')


if 3 > 1 and 3 > 2:
    print('and operator')


if 4 > 2 or 3 > 1:
    print('or  operator')


x = 20
if not x > 20:
    print('not in python')


print('\n')

print('________________________________________________________________')
print('\n')
print('*** Membership Operators in Python ***')
print('\n')

if 'i' in 'String':
    print('in in python')

if 'i' not in 'Apple':
    print('not in in python')

print('\n')

print('________________________________________________________________')
print('\n')
print('*** Identity Operators in Python ***')
print('\n')


if (2 > 1) is True:
    print('is true')

if (1 > 10) is not True:
    print('is not true')


x = input('Enter the number')
print(int(x) ** 2)


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
"""

hello = "Hello"
Hello_List = [1, 2, 3, "hello", "List"]
hello_Tuple = (1, 2, 3, "hello", "list")


print(type(hello))
print(type(Hello_List))
print(type(hello_Tuple))
