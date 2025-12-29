from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
mon_machine = MoneyMachine()
menu = Menu()


while True:
    print("Welcome to the coffee machine!")

    order = input(f"What would you like to order?\n{menu.get_items()}: ").lower()

    if order == "report":
        coffee_machine.report()
        mon_machine.report()

    elif order == "off":
        exit()

    else:
        if menu.find_drink(order):
            choice = menu.find_drink(order)
            if coffee_machine.is_resource_sufficient(choice):
                if mon_machine.make_payment(choice.cost):
                    coffee_machine.make_coffee(choice)
        





