import random
from art import logo,vs
from game_data import data

score = 0

a_data = data[random.randint(0, len(data))]
b_data = data[random.randint(0, len(data))]
if a_data == b_data:
    b_data = data[random.randint(0,len(data))]
game_over = False
print(logo)
while not game_over:

    b_data = data[random.randint(0, len(data))]
    print(f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}.")
    print(vs)
    print(f"Against B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(logo)
    if (a_data['follower_count'] > b_data['follower_count'] and user_choice == 'a') or (b_data['follower_count'] > a_data['follower_count'] and user_choice == 'b'):
        score += 1
        print(f"You're right! Current score : {score}")
    elif (a_data['follower_count'] > b_data['follower_count'] and user_choice == 'b') or (b_data['follower_count'] > a_data['follower_count'] and user_choice == 'a'):
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True

    a_data = b_data