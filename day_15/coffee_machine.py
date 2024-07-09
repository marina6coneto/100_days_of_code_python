MENU = {
    'espresso':{
        'ingredients':{
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte':{
        'ingredients':{
            'water': 200,
            'coffee': 24,
            'milk': 150,
        },
        'cost': 2.5,
    },
    'cappuccino':{
        'ingredients':{
            'water': 250,
            'coffee': 24,
            'milk': 100,            
        },
        'cost': 3.0,
    }
}

profit = 0

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}


def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made,
    False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry, there is not enough {item}')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins.')
    total = 0
    try:
        quarters = int(input('How many quarters?: '))
        if quarters < 0:
            raise ValueError("Please enter a positive number.")
        total += quarters * 0.25
        
        dimes = int(input('How many dimes?: '))
        if dimes < 0:
            raise ValueError("Please enter a positive number.")
        total += dimes * 0.1
        
        nickels = int(input('How many nickels?: '))
        if nickels < 0:
            raise ValueError("Please enter a positive number.")
        total += nickels * 0.05
        
        pennies = int(input('How many pennies?: '))
        if pennies < 0:
            raise ValueError("Please enter a positive number.")
        total += pennies * 0.01
        
    except ValueError as e:
        print(f"Invalid input: {e}")
        return process_coins()  # Recursively calls if there is a problem
    
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted,
    or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name}! ☕')


is_on = True

while is_on:
    choice = input(
        'What would you like? (espresso/latte/cappuccino/report/off): '
    ).strip().lower()
    
    while choice not in ["espresso", "latte", 'cappuccino', 'report', 'off']:
        print('Invalid input.')
        print('Please type (espresso/latte/cappuccino/report/off).')
        choice = input(
            'What would you like? (espresso/latte/cappuccino/report/off): '
        ).strip().lower()
    
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print("----- Report -----")
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
        print("------------------")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])