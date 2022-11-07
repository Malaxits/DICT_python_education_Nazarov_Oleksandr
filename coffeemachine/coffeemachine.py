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