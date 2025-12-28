'''
Day 15: Coffee machine
'''


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
            "milk": 50,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


wallet = {
    "quarter": {
        "value": 0.25,
        "quantity": 4,
    },
    "dime": {
        "value": 0.10,
        "quantity": 4,
    },
    "nickel": {
        "value": 0.05,
        "quantity": 4,
    },
    "penny": {
        "value": 0.01,
        "quantity": 4
    }
}

# print(type(wallet["quarter"]["value"]))x


def count_money(q,d,n,p):
    q_value = q * wallet["quarter"]["value"]
    d_value = d * wallet["dime"]["value"]
    n_value = n * wallet["nickel"]["value"]
    p_value = p * wallet["penny"]["value"]
    total = round(sum((q_value, d_value, n_value, p_value)),2)
    return total



def show_report():
    mon = count_money(q=wallet["quarter"]["quantity"],
                      d=wallet["dime"]["quantity"],
                      n=wallet["nickel"]["quantity"],
                      p=wallet["penny"]["quantity"])

    print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${mon}
""")


def check_resources(order):
    for ingredient, amount in MENU[order]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True    





while True:

    order = ""
    while order not in ("espresso", "latte", "cappuccino", "report", "off"):
        order = input("What would you like?\n(espresso, latte, cappuccino): ").lower()

    if order == "report":
        show_report()
    elif order == "off":
        exit()
    else:
        check = check_resources(order)

        if check:
            print("Please enter coins to purchase your drink")
            q_add = int(input("How many quarters will you add?: "))
            d_add = int(input("How many dimes will you add?: "))
            n_add = int(input("How many nickels will you add?: "))
            p_add = int(input("How many pennies will you add?: "))
            check_payment = count_money(q=q_add,
                                        d=d_add,
                                        n=n_add,
                                        p=p_add)
            if check_payment < MENU[order]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                wallet["quarter"]["quantity"] += q_add
                wallet["dime"]["quantity"] += d_add
                wallet["nickel"]["quantity"] += n_add
                wallet["penny"]["quantity"] += p_add
                
                change_owed = check_payment - MENU[order]["cost"]
                change_given = 0

                while change_owed >= wallet["quarter"]["value"] and wallet["quarter"]["quantity"] > 0:
                    wallet["quarter"]["quantity"] -= 1
                    change_given += wallet["quarter"]["value"]
                    change_owed -= wallet["quarter"]["value"]

                while change_owed >= wallet["dime"]["value"] and wallet["dime"]["quantity"] > 0:
                    wallet["dime"]["quantity"] -= 1
                    change_given += wallet["dime"]["value"]
                    change_owed -= wallet["dime"]["value"]

                while change_owed >= wallet["nickel"]["value"] and wallet["nickel"]["quantity"] > 0:
                    wallet["nickel"]["quantity"] -= 1
                    change_given += wallet["nickel"]["value"]
                    change_owed -= wallet["nickel"]["value"]

                while change_owed >= wallet["penny"]["value"] and wallet["penny"]["quantity"] > 0:
                    wallet["penny"]["quantity"] -= 1
                    change_given += wallet["penny"]["value"]
                    change_owed -= wallet["penny"]["value"]


                if change_given > 0:
                    change_given = round(change_given,2)
                    print(f"Here is your change: ${change_given}")

                change_owed = 0
                change_given = 0

                for ingredient, amount in MENU[order]["ingredients"].items():
                    resources[ingredient] -= amount

                print(f"Here is your {order}. Enjoy!")







