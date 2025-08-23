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


# Dictionary Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
# passed_students = {student:student_scores[student] for student in student_scores if student_scores[student] > 60}
passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
print(passed_students)

# Looping through a DataFrame
student_dict = {"student": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
                "score": [43, 75, 84, 26, 65,64]}
student_df = pandas.DataFrame(student_dict)
for (key, value) in student_df.items():
    print(f"Key: \n{key}")
    print(f"Values: \n{value}")

# Looping through the rows of a DataFrame
for (index, row) in student_df.iterrows():
    if row.student == "Beth":
        print(row.score)