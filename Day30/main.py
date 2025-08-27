# FileNotFoundError:
# with open("file_name.txt") as file:
#     file.read()

# KeyError
# dictionary = {"key": "value"}
# value = dictionary["non_existent_key"]

# IndexError
# items_list = ["Apple", "Mango", "Banana"]
# fruit = items_list[4]

# TypeError
# text = "sdfj"
# print(text + 7)


# Handling errors
try:
    file = open("file_name.txt")
    dictionary = {"key": "value"}
    value = dictionary["non_existent_key"]
except FileNotFoundError:
    file = open("file_name.txt", "w")
    file.write("Text in the file")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
else:   # else is executed only if the try block doesn't throw any error i.e, try block is fully executed successfully
    content = file.read()
    print(content)
finally:
    # raise TypeError("This is an error which is raised by the user")
    file.close()
    print("File is closed")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)