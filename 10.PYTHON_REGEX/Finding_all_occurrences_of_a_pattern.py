"""
re.findall() : Return all non-overlapping matches of pattern in string, as a list of strings.
The string is scanned left-to-right, and matches are returned in the order found

"""

import re

# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and
             my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)


# Python Regex: re.search() VS re.findall()

"""
    re.search()
    ___________
    
re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, 
so this is best suited for testing a regular expression more than extracting data.

"""
