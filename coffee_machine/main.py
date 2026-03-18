#----------coffe machine-------------

MENU = {
    "espresso" : {
        "ingredient" : {
        "water" : 58,
        'coffee': 18
        },
        'cost': 1.5,
    },
    "latte" : {
        "ingredient": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
            },
        "cost" : 2.5
    },
    "capppuccino" : {
        'ingredient':{
            "water" : 250,
            'milk': 100,
            'coffee':24,
        },
        "cost": 3.0
        
    }
    
}
profit = 0
resources = {
    "water" : 300,
    'milk' : 200,
    "coffee" : 100,
}


def is_resoure_sufficient(order_ingredient):
    
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """returne the total calculated form coins inserted"""
    
    print("pleas insert coins")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickels? ")) * 0.5
    total += int(input("how many pennies? ")) * 0.1
    return total


def is_transaction_seccesful(mony_recevied, drink_cost):
    
    if mony_recevied >= drink_cost:
        change = round(mony_recevied - drink_cost, 2)
        print(f"here is the cash u inserted ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorrt that is not enough money. ")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is ur {drink_name}")        



is_on =True

while is_on:
    choice = input("what u like (capppuccino/latte/espresso) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
            print(f"water : {resources['water']}ml")
            print(f"milk :{resources['milk']}ml ")
            print(f"coffee :{resources['coffee']}g ")
            print(f"money : {profit}")
    else:
        dirnk = MENU[choice]
        if is_resoure_sufficient(dirnk["ingredient"]):
            payment = process_coins()
            if is_transaction_seccesful(payment, dirnk["cost"]):
                make_coffee(choice, dirnk["ingredient"])

