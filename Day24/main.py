# file = open("my_file.txt")  -->   default mode is "r"
# contents = file.read()
# print(contents)
# file.close()


# C:\Users\pooji\OneDrive\Desktop   --> path of my text file named "new_file.txt"
# C:\Users\pooji\PycharmProjects\PythonProject\day24  --> path of my "main.py" file

with open("../../../OneDrive/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("my_file.txt", mode="a") as file:
#     contents = file.write("\nNew text added")

# if we try to open a file in write mode and write, then it replaces the existing contents with the new one

# if the file we are trying to write doesn't exist, then python creates one for us (this only works in "w" mode and if file doesn't exist):
# with open("new_file.txt", mode="w") as f:
#     content = f.write("New file contents here!")