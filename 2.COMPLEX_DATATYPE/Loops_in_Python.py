# The for loop
for [ELEMENT] in [ITERATIVE-LIST]:
    [statement to execute]
else:
    [statement to execute when loop is over]
    [else statement is completely optional]


# The while loop

while [condition]:
    [statement to execute]
else:
    [statement to execute if condition is false]
    [else statement is completely optional]


# The continue keyword

name = "StudyTonight"
for i in name:
    continue
    print(i)


# The break keyword

for i in name:
    if i == "T":
        break
    print(i)
