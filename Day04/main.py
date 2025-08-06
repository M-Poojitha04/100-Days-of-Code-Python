import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
your_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
list1 = [rock,paper,scissors]
if your_choice >= 3 or your_choice < 0:
    print("You chose an invalid number! Try again")
else:
    print("You chose: "+ list1[your_choice])

    comp_choice = random.randint(0,2)
    print("Computer chose:"+list1[comp_choice])

    if your_choice and comp_choice == (0 or 1 or 2):
        print("It's a Draw!")
    elif your_choice == 0 and comp_choice == 1:
        print("Computer wins")
    elif your_choice == 1 and comp_choice == 2:
        print("Computer wins")
    elif your_choice == 2 and comp_choice == 0:
        print("Computer wins")
    else:
        print("You won!")