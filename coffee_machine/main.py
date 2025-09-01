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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]

def check_resources(coffee_choice):
    for item, amount in MENU[coffee_choice]["ingredients"].items():
        if resources.get(item, 0) < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

money = 0.00

while True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if coffee_choice == "report":
            print(f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml'
                  f'\nCoffee: {resources["coffee"]} g\nMoney: ${money}')
    elif coffee_choice in MENU:
        if not check_resources(coffee_choice):
            continue
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total_coins = quarters + dimes + nickels + pennies
        if coffee_choice == "espresso" and total_coins < espresso_cost:
            print("Sorry, that's not enough money. Money refunded.")
        elif coffee_choice == "latte" and total_coins < latte_cost:
            print("Sorry, that's not enough money. Money refunded.")
        elif coffee_choice == "cappuccino" and total_coins < cappuccino_cost:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            print(f"Here is your {coffee_choice} ☕️. Enjoy!")
            refund = total_coins - MENU[coffee_choice]["cost"]
            print(f"Here is your change: ${(round(refund, 2))}")
            if coffee_choice == "espresso":
                resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
                resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
                money += MENU[coffee_choice]["cost"]
            else:
                resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
                resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
                money += MENU[coffee_choice]["cost"]
    elif coffee_choice == "off":
        break
    else:
        print("Sorry, you typed in a non-existent drink.")









