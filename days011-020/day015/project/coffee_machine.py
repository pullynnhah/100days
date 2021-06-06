def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money:.2f}')


def check_resources(drink):
    resources_needed = drink['ingredients']

    for resource, amount in resources_needed.items():
        if resources[resource] < amount:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def process_payment(drink):
    price = drink['cost']

    print("Please insert coins.")
    total = 0.0
    for coin, value in coins.items():
        total += float(input(f'How many {coin}? ')) * value
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if total > price:
        print(f"Here is ${total - price:.2f} in change.")
    return True


def change_resources(drink):
    global resources, money
    resources_needed = drink['ingredients']
    price = drink['cost']
    for resource, amount in resources_needed.items():
        resources[resource] -= amount
    money += price


def make_coffee(drink_name):
    drink = MENU[drink_name]
    if check_resources(drink) and process_payment(drink):
        print(f"Here is your {drink_name} ☕️. Enjoy!")
        change_resources(drink)


def coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        return
    if user_choice == 'report':
        report()
    else:
        make_coffee(user_choice)
    coffee_machine()


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

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}
money = 0.0

coffee_machine()
