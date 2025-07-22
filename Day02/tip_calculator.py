print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
calc_tip = 1 + (tip / 100)
divided = bill/people
calc_total = divided * calc_tip
total = round(calc_total,2)
print(f"The final bill is : ${total} ")