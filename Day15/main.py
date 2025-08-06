MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money= 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def check_resources(ingredient):
    for item in ingredient:
        if ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(drink):
    global money
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total_money = quarters + dimes + nickles + pennies
    if total_money >= MENU[drink]["cost"]:
        change = round(total_money - MENU[drink]["cost"])
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        for item in MENU[drink]["ingredients"]:
            resources[item] -= MENU[drink]["ingredients"][item]
        money += MENU[drink]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")


machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        machine_on = False

    elif user_choice == 'report':
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money}")

    elif user_choice == 'espresso' or 'latte' or 'cappuccino':
        if check_resources(MENU[user_choice]["ingredients"]):
            make_coffee(user_choice)