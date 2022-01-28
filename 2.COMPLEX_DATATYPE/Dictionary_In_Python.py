#  creating a dictionary

myDictionary = {'Key-1': 'Element-1', 'Key-2': 'Element-2',
                'Key-3': 'Element-3', 'Key-4': 'Element-4'}

print(myDictionary['Key-3'])

# To create an empty dictionary, do the following:

emptyList = {}

emptyList["India"] = "Delhi"

print(emptyList)

# Accessing elements of a dictionary

for i in myDictionary:
    print("Key: " + i + " and Element: " + myDictionary[i])

# Deleting element(s) in a dictionary
identity = {"name": "StudyTonight", "type": "Educational",
            "link": "http://studytonight.com", "tag": "Best place to learn"}
del identity["link"]
print(identity)

# Appending element(s) to a dictionary

# identity["email": "we@studytonight.com"]
# print (identity)

# Updating existing element(s) in a dictionary

courseAvail = {"Java": "Full-course",
               "C/C++": "Full-course", "DBMS": "Full-course"}
identity.update(courseAvail)

print(courseAvail)
print(identity)


# Dictionary Functions in Python
len()
clear()
values()
keys()
items()
__contains__
# In case you ever need to compare two dictionaries
cmp()



