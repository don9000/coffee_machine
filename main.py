import menu

initial_levels = menu.resources

def adjust_profits(selection):
    current_total = menu.profit
    current_total += menu.MENU[selection]['cost']
    menu.profit = current_total

def resource_management(current_levels, choice):
    if choice != 'espresso':
        current_levels['water'] -= menu.MENU[choice]['ingredients']['water']
        current_levels['milk'] -= menu.MENU[choice]['ingredients']['milk']
        current_levels['coffee'] -= menu.MENU[choice]['ingredients']['coffee']
    else:
        current_levels['water'] -= menu.MENU[choice]['ingredients']['water']
        current_levels['milk'] -= 0
        current_levels['coffee'] -= menu.MENU[choice]['ingredients']['coffee']
    return current_levels

def determine_sufficient_quantities(choice, current_levels):
    req_water = menu.MENU[choice]['ingredients']['water']
    req_coffee = menu.MENU[choice]['ingredients']['coffee']
    rem_water = current_levels['water']
    rem_milk = current_levels['milk']
    rem_coffee = current_levels['coffee']
    if choice != 'espresso':
        req_milk = menu.MENU[choice]['ingredients']['milk']
    elif choice == 'espresso':
        req_milk = 0
    if rem_coffee >= req_coffee and rem_water >= req_water and rem_milk >= req_milk:
        return True
    else:
        return False    

def coin_counter(selection):
    quaters = int(input("number of quaters: "))
    dimes = int(input("number of dimes: "))
    nickels = int(input("number of nickels: "))
    pennies = int(input("number of pennies: "))
    total = quaters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01 
    clean_total = round(total, 2)
    cost = menu.MENU[selection]['cost']
    change = clean_total - cost
    if cost < clean_total:
        print(f"You deposited {clean_total} and the cost of the  {selection} is {cost}, your change is {round(change,2)}")
        adjust_profits(selection)
    else: 
        print(f"The cost of a {selection} is {cost} you have only deposted {clean_total}, your money has been refunded ")


def coffee_machine():
    selection = ""
    levels_sufficient = True
    current_levels = initial_levels
    while selection != 'off' and levels_sufficient:
        selection = input("espresso, latte or cappuccino? ")
        if selection == "off":
            break
        elif selection == "report":
            profit = menu.profit
            print(f"current levels are {current_levels} and profit is {profit}")
        else:
            levels_sufficient = determine_sufficient_quantities(selection, current_levels)
            current_levels = resource_management(current_levels, selection)            
            if levels_sufficient:
                coin_counter(selection)               
            else:
                print("There does not seem to be enough ingredients for your order")    


        # current_levels = resource_management(current_levels,)
        # think about usig an if statement for the levels

coffee_machine()
# coin_counter("latte")

