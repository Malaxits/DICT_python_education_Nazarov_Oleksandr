class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    money = 550
    cups = 9
    status ="wait"
    status = "wait"
    counter = 0
    def __make_coffee(coffee, take_money, need_water, need_coffee, need_milk=0):
        if coffee.water < need_water:
            print("Sorry, not enough water!")
        elif coffee.coffee < need_coffee:
            print("Sorry, not enough coffee!")
        elif coffee.milk < need_milk:
            print("Sorry, not enough milk!")
        elif coffee.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            coffee.water -= need_water
            coffee.coffee -= need_coffee
            coffee.milk -= need_milk
            coffee.cups -= 1
            coffee.money += take_money
    def action(changes, command):
        if command == "buy":
            changes.status = "make"
        elif command == "fill":
            changes.status = "fill"
            changes.counter = 0
        elif command == "take":
            print(f"I gave you {changes.money}")
            changes.money = 0
        elif command == "remaining":
            print("The coffee machine has:")
            print(f"{changes.water} of water")
            print(f"{changes.milk} of milk")
            print(f"{changes.coffee} of coffee")
            print(f"{changes.cups} of disposable cups")
            print(f"{changes.money} of money")
        elif changes.status == "make":
            try:
                type_of_coffee = int(command)
            except:
                type_of_coffee = 4
            if type_of_coffee == 4:
                changes.status = "wait"
                return
            elif type_of_coffee == 1:
                changes.__make_coffee(4, 250, 16)
            elif type_of_coffee == 2:
                changes.__make_coffee(7, 350, 20, 75)
            elif type_of_coffee == 3:
                changes.__make_coffee(6, 200, 10, 100)
            changes.status = "wait"
        elif changes.status == "fill":
            v = int(command)
            if changes.counter == 0:
                changes.water += v
            elif changes.counter == 1:
                changes.coffee += v
            elif changes.counter == 2:
                changes.milk += v
            elif changes.counter == 3:
                changes.cups += v
                changes.status = "wait"
                changes.counter = -1
            changes.counter += 1
        else:
            changes.status = "wait"
coffee_machine = CoffeeMachine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n>")
    coffee_machine.action(action)
    if action == "buy":
        type_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to menu:\n>")
        coffee_machine.action(type_of_coffee)
    elif action == "fill":
        water = input("Write how many ml of water you want to add:\n>")
        coffee_machine.action(water)
        milk = input("Write how many ml of milk you want to add:\n>")
        coffee_machine.action(milk)
        coffee = input("Write how many grams of coffee beans you want to add:\n>")
        coffee_machine.action(coffee)
        cups = input("Write how many disposable coffee cups you want to add:\n>")
        coffee_machine.action(cups)
    elif action == "exit":
        break
