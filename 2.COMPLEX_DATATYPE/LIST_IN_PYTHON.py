myEmptyList = []

myIntegerList = [9, 4, 3, 2, 8]

myFloatList = [2.0, 9.1, 5.9, 8.123432]

myCharList = ['p', 'y', 't', 'h', 'o', 'n']

myStringList = ["Hello", "Python", "Ok done!"]

# Deriving from another List
myList1 = ['first', 'second', 'third', 'fourth', 'fifth']
myList2 = myList1

print(myList2)

# Use slicing, for copying only the first three elements,
myList2 = myList1[0:3]
print(myList2)

myList2 = myList1[-3]
print(myList2)

# Adding Serial Numbers in a List
"""
Suppose you want to add serial whole numbers
(i.e., 0, 1, 2, 3, ...) into your list and just don't want to write all of them one by one, do not worry, there is a shortcut for doing this.
"""

myList1 = range(9)
myList1 = range(5, 9)

myQuickList = [x**2 for x in range(5)]

print(myQuickList)

# Appending to a List
emptyList = []
emptyList.append('The Big Bang Theory')
emptyList.append('F.R.I.E.N.D.S')
emptyList.append('How I Met Your Mother')
emptyList.append('Seinfeld')

print(emptyList)

# Utilising list elements in Python
for x in range(0, 5):
    print(x)


i = 0
while i < 5:
    print(i)
    i = i+1

# Using Loops with List

myList = ['Last Of Us', 'Doom', 'Dota', 'Halo', ' ']
for x in myList:
    print(x)

# Iterate two Lists simultaneously to add them and save it in the third List

i = 0
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = []
while i < len(A):
    C.append(A[i]+B[i])
    i = i+1

# Iterate two Lists simultaneously - zip() method

A = [9, 8, 7, 6, 5]
B = [3, 4, 5, 6, 7]
C = []
for x, y in zip(A, B):
    C.append(x+y)

print(C)

# Another approach to this problem could have been using the index number of the list A and B.

for i in range(0, 5):
    C.append(A[i]+B[i])
print(C)

# Deleting an element from a List

myList.pop(4)
del myList[4]
del myList[3:7]


#  remove functions from the list
myList = ['Apple', 'Orange', 'Apple', 'Guava']
myList.remove('Apple')


# Convert a List to String

mylist1 = ['butter', 'jam', 'curd']
myStr = ', '.join(mylist1)
print(myStr)


# More functions for Lists

myList = ['Python', 'C++', 'Java', 'Ruby', 'Perl']
myList.insert(1, 'JavaScript')
print(myList)


# reverse
myList.reverse()

# sort
myList.sort()

# sort reverse
myList.sort().reverse()
