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
    "money": 0.0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def get_user_input():
    is_typo = True

    while is_typo:
        user_input = input("What would you like? Choose between 'espresso', 'latte' or 'cappuccino': ")

        if user_input == "off" or user_input == "report" or user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            return user_input
        else:
            print("You typed incorrectly. Please, try again.")


def get_coffee(selected_drink):
    drink = MENU[selected_drink]

    unavailable_ingredients = []

    for ingredient in drink["ingredients"]:
        resource_needed = drink["ingredients"][ingredient]
        resource_stored = resources[ingredient]

        if resource_needed > resource_stored:
            unavailable_ingredients.append(ingredient)
        elif resource_stored >= resource_needed:
            if len(unavailable_ingredients) == 0:
                resources[ingredient] = resource_stored - resource_needed

    if len(unavailable_ingredients) == 0:
        return True
    if len(unavailable_ingredients) == 1:
        print(f"Sorry, there isn't enough {unavailable_ingredients[0]}.")
    if len(unavailable_ingredients) == 2:
        print(f"Sorry, there isn't enough {unavailable_ingredients[0]} and {unavailable_ingredients[1]}.")
    if len(unavailable_ingredients) == 3:
        print(f"Sorry, there isn't enough {unavailable_ingredients[0]}, {unavailable_ingredients[1]} and {unavailable_ingredients[2]}.")
    return False


def get_payment(selected_drink):
    bill = MENU[selected_drink]["cost"]

    formatted_bill = format(bill, ".2f")  # this gives 2 decimals to the value
    print(f"The drink costs ${formatted_bill}. Please, insert coins.")

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    money = quarters + dimes + nickles + pennies

    if bill > money:
        formatted_difference = format(bill - money, ".2f")
        print(f"You don't have enough money. Money refunded. You need more ${formatted_difference}.")
        return False
    elif money >= bill:
        # This adds money to the coffee machine resources storage
        resources["money"] += bill
        change = money - bill

        if change == 0:
            print("Thanks!")
        elif change > 0:
            formatted_change = format(change, ".2f")  # this gives 2 decimals to the value
            print(f"Thanks! Here is ${formatted_change} in change.")
        return True


is_on = True

while is_on:

    user_choice = get_user_input()

    if user_choice == "off":
        is_on = False
        print("Machine now is turned off.")
    elif user_choice == "report":
        print_report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        has_resources = get_coffee(selected_drink=user_choice)

        if has_resources:
            has_money = False

            while not has_money:
                has_money = get_payment(selected_drink=user_choice)

            print(f"Here is your {user_choice} ☕. Enjoy!")
