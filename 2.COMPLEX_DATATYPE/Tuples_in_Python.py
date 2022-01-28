# Defining a Tuple
myTuple = 1, 2, 3, 4

print(type(myTuple))

# You can obviously add data of different types in a single tuple,

secondTuple = 1, 2, "python", 4
print(secondTuple)


# An empty tuple can be created using the tuple() function or by just using an empty bracket ().

emptyTuple = ()
anotherEmptyTuple = tuple()

# Indexing in Tuples
example = "apple", "orange", "banana", "berry", "mango"
print(example[0])

# Adding Elements to a Tuple
t = (1, 2, 3, 4, 5)
t = t + (7,)
print(t)


# Deleting a Tuple
del (myTuple)

# Slicing in Tuples
t = (1, 2, 3, 4)
print(t[2:4])

# Multiplication

t = (2, 5)
print(t*3)


# Addition

t = (2, 5, 0) + (1, 3) + (4,)
print(t)


# in keyword
t = (1, 2, 3, 6, 7, 8)
2 in t
5 in t

# len() function
t = 1, 2, 3
print(len(t))


# cmp() function, is used to compare two tuples


# max() and min() function
# To find the maximum value in a tuple, we can use the max() function, while for finding the minimum value, min() function can be used.
