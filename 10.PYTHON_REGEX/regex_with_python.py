"""
A regular expression is a sequence of characters that forms a search pattern to find a match in a string ro a set of strings.

It can be used to check if a string contains a certain pattern, or to extract portions of a string that match a pattern.
It can detect the absence or presence or absence of a pattern in a string.
It can also be used to find the location of a pattern in a string.

"""
import re

s = 'GeeksforGeeks: A computer science portal for geeks'

match = re.search(r'Geeks', s)

#  start() method returns the starting position of the match
print(match.start())
# end() method returns the ending position of the match
print(match.end())

# \ backslash is used to escape the special characters
# here backslash is used to escape the special characters .
s = 'geeks.forgeeks'

# without using \
match = re.search(r'.', s)
print(match.start())

# using \
match = re.search(r'\.', s)
print(match.start())


# [] is used to specify a set of characters
# here [aeiou] means any character from aeiou
# here [a-z] means any character from a to z
# here [0-9] means any character from 0 to 9
# here [^aeiou] means any character except aeiou
# here [^a-z] means any character except a to z
# here [^0-9] means any character except 0 to 9

"""Square Brackets ([]) represents a character class consisting of a set of characters that we wish to match. For example, the character class [abc] will match any single a, b, or c. 

We cal also specify a range of characters using – inside the square brackets. For example, 

[0, 3] is sample as [0123]
[a-c] is same as [abc]

"""

# s = 'GeeksforGeeks: A computer science portal for geeks'
match = re.search(r'[g-q]', s)

print(match.start())


# ^ means any character except the characters specified in the square brackets
"""
^ – Caret
Caret (^) symbol matches the beginning of the string i.e. checks whether the string starts with the given character(s) or not. For example –  

^g will check if the string starts with g such as geeks, globe, girl, g, etc.
^ge will check if the string starts with ge such as geeks, geeksforgeeks, etc.
"""

match = re.search(r'^gee', s)
print(match.start())


# $ – Dollar matches the end of the string i.e.
# checks whether the string ends with the given character(s) or not. For example –
# $g will check if the string ends with g such as geeks, globe,

"""
$ – Dollar

Dollar($) symbol matches the end of the string i.e checks whether the string ends with the given character(s) or not. For example – 

s$ will check for the string that ends with a such as geeks, ends, s, etc.
ks$ will check for the string that ends with ks such as geeks, geeksforgeeks, ks, etc.

"""
p = 'computer science portal for geeks'
match = re.search(r'ks$', p)
print(match.start())
print(match.end())


"""
. – Dot
Dot(.) symbol matches only a single character except for the newline character (\n). For example –  

a.b will check for the string that contains any character at the place of the dot such as acb, acbd, abbb, etc
.. will check if the string contains at least 2 characters

"""
match = re.search(r'..', s)
print(match.start())

s = 'GeeksforGeeks: A computer science portal for geeks'

"""
| – Or
Or symbol works as the or operator meaning it checks whether the pattern before or after the or symbol is present in the string or not. For example –  

a|b will match any string that contains a or b such as acd, bcd, abcd, etc.

"""
match = re.search(r'hero | A', s)

print(match.start())


"""
? – Question Mark
Question mark(?) checks if the string before the question mark in the regex occurs at least once or not at all. For example –  

ab?c will be matched for the string ac, acb, dabc but will not be matched for abbc because there are two b. Similarly, it will not be matched for abdc because b is not followed by c.

"""

"""
* – Star
Star (*) symbol matches zero or more occurrences of the regex preceding the * symbol. For example –  

ab*c will be matched for the string ac, abc, abbbc, dabc, etc. but will not be matched for abdc because b is not followed by c.
"""

