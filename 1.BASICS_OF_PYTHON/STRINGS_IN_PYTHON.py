str1 = "This is not my first String"
print(str)

"""[Operations on String]
"""

# Concatenation
print("Hello" + "World")

# Repetition
print("Hi!" * 100)

# Check existence of a character or a sub-string in a string
print("won" in "India won the match")

# not in keyword
print("won" not in "India won the match")

# Converting String to Int or Float datatype and vice versa
numStr = '123'
numFloat = float(numStr)
numInt = int(numFloat)
print(numFloat)
print(numInt)

# Slicing
str = "Hello Brother!"
print(str[0:10:2])


#  length of string
s = "Hello"
print(len(s))

# find(subString)
s = "Hello"
ss = "He"
print(s.find(ss))

print ("Hello, World".upper())
print ("hello, world".islower())

print ("Hello, World".replace("World", "India"))

# string_name.split(character, integer)
mystring = "Hello World! Welcome to the Python tutorial"
print (mystring.split("!"))

