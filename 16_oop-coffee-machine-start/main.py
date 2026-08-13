from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
machine_running = True

while machine_running:
    prompt = str(input("“What would you like? (espresso/latte/cappuccino/):"))

    match prompt.lower():
        case "off":
            machine_running = False
            print("Machine turned off.")
        case "report":
            coffee_maker.report()
            continue
        case _:
            drink_item = menu.find_drink(prompt)
            if drink_item:
                if coffee_maker.is_resource_sufficient(drink_item):
                    payment_done = money_machine.make_payment(drink_item.cost)
                    if payment_done:
                        coffee_maker.make_coffee(drink_item)
                    else:
                        continue
                else:
                    continue
            else:
                continue