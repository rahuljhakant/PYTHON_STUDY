# Structure of function definition

# def functionName(parameter1, parameter2, ...):
#     logic/algorithm statements
#     ...
#     return someData


# def add(a, b):
#     c = (a+b)
#     return c

def findalltheintegercharacterinastring(str):
    count = 0
    for i in str:
        if i.isdigit():
            count += 1
    return count


print(findalltheintegercharacterinastring('1234'))