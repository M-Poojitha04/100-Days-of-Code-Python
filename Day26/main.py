# List Comprehension
num = [1,2,3]
new_num = [n+1 for n in num]
print(new_num)

name = "Pooja"
new_list = [letter for letter in name]
print(new_list)

range_list = [r * 2 for r in range(1, 5)]
print(range_list)

# Conditional List Comprehension
names = ["one", "two", "three", "four", "five", "six"]
new_names = [name for name in names if len(name) < 4]
print(new_names)
upper_case_names = [n.upper() for n in names if len(n) >= 4]
print(upper_case_names)