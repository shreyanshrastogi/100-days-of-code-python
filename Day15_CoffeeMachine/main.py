
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
machine_dollar=0
def coffee_machine():
    global machine_dollar
    customer_dollar =0
    drink= input("What would you like? (espresso/latte/cappuccino)").strip().lower()
    #off
    if drink=="off":
        return False
    #report
    elif drink=="report":
        print(resources)
        return True
    elif drink not in MENU:
        print("drink not in menu")
        return True
    #check resources
    for key in resources:
        if resources[key]<MENU[drink]["ingredients"][key]:
            print("not enough "+key+".")
            print("next customer")
            return True
    print("insert coin:")
    try:
        customer_dollar +=float(input("enter Quarters:").strip())*.25
        customer_dollar +=float(input("enter Dime:").strip())*.10
        customer_dollar +=float(input("enter Nickle:").strip())*.05
        customer_dollar +=float(input("enter Penny:").strip())*.01
    except ValueError:
        print("wrong datatype.")
        return True

    #checking money
    if customer_dollar<MENU[drink]["cost"]:
        print("not enough money")
        print("here is your refund:",customer_dollar)
    elif customer_dollar>MENU[drink]["cost"]:
        print("here is your change:",customer_dollar-MENU[drink]["cost"])
    #providing coffee and store money
    if customer_dollar>=MENU[drink]["cost"]:
        machine_dollar += MENU[drink]["cost"]
        #making coffee and decreasing resources
        for key in resources:
            resources[key]-=MENU[drink]["ingredients"][key]
        #giving coffee
        print(f"here is your {drink}.")

    print("next customer.")
    return True


on =True
while on:
    on=coffee_machine()























