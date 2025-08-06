import random
import art

new_game = True

def card_sum(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0  # Represents a Blackjack
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)

def printing_scores():
    print(f"Your final hand: {user_cards}, final score: {card_sum(user_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score: {card_sum(comp_cards)}")

def check_comp_cards():
    while card_sum(comp_cards) < 17:
        comp_cards.append(random.choice(cards))

while new_game:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == 'y':
        print("\n" * 25)
        print(art.logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = []
        comp_cards = []

        for _ in range(2):
            user_cards.append(random.choice(cards))
            comp_cards.append(random.choice(cards))

        user_score = card_sum(user_cards)
        comp_score = card_sum(comp_cards)

        if user_score == 0 and comp_score == 0:
            printing_scores()
            print("Draw 🙃")
            continue_game = False
        elif user_score == 0:
            printing_scores()
            print("Win with a Blackjack 😎")
            continue_game = False
        elif comp_score == 0:
            printing_scores()
            print("Lose, opponent has Blackjack 😱")
            continue_game = False
        elif user_score > 21:
            printing_scores()
            print("You went over. You lose 😭")
            continue_game = False
        else:
            continue_game = True
            while continue_game:
                print(f"Your cards: {user_cards}, current score: {card_sum(user_cards)}")
                print(f"Computer's first card: {comp_cards[0]}")
                continue_or_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                if continue_or_pass == 'y':
                    user_cards.append(random.choice(cards))
                    if card_sum(user_cards) > 21:
                        print(f"Your cards: {user_cards}, current score: {card_sum(user_cards)}")
                        printing_scores()
                        print("You went over. You lose 😭")
                        continue_game = False
                elif continue_or_pass == 'n':
                    check_comp_cards()
                    user_score = card_sum(user_cards)
                    comp_score = card_sum(comp_cards)

                    if comp_score > 21:
                        printing_scores()
                        print("Opponent went over. You win 😁")
                    elif user_score > comp_score:
                        printing_scores()
                        print("You win 😃")
                    elif user_score < comp_score:
                        printing_scores()
                        print("You lose 😤")
                    else:
                        printing_scores()
                        print("Draw 🙃")
                    continue_game = False
    else:
        new_game = False
