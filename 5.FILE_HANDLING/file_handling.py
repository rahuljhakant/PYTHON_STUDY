myFile = open("file.txt")

myFile1 = open("C:/c_code/file.txt")

# read mode - "r"
myFile2 = open("file.txt", "r")

# write mode - "w"
myFile = open("file.txt", "w")

# append mode - "a"
myFile = open("file.txt", "a")


# read/write mode - "r+" or "w+"
myFile = open("file.txt", "r+")

# append/read - "a+"

myFile = open("file.txt", "a+")

# close the file after use
myFile.close()



# Reading a File

myFile.readline()

for line in myFile:
    # will print all the lines one by one
    print (line)



content = myFile.readlines()

content = "Hello, World. I am learning Python."

myFile.write(content)

myFile.write("Hello, World. I am learning Python")