from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on  = True

while is_on:
    options = menu.get_items()
    
    choice = input(
            f'What would you like? ({options}report/off): '
        ).strip().lower()
    
    while choice not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        print('Invalid input.')
        print('Please type (espresso/latte/cappuccino/report/off).')
        choice = input(
            f'What would you like? ({options}report/off): '
        ).strip().lower()
    
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drinks(choice)
        if coffee_maker.is_resources_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)