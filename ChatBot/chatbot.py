print("Hello! My name is Van \n I was created in 2022.")
print("Please, remind me your name:")
name = input(">")
print(f"What a great name you have,{name}")
print("Let me guess your age? \nEnter remainders of dividing your age by 3, 5 and 7")
remainder3 =int(input(">"))
remainder5 =int(input(">"))
remainder7 =int(input(">"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is",age,"that`s good time to start programming! ")
a = int(input("Now I will prove to you that I can count to any number you want.\n"))
for i in range(a +1):
    print(str(i)+ "!")
print("Completed,Have a nive day!")
print("Let`s test you.\nWhat is my name? ")
print("1.Van! \n2. Billy!")
while True:
    k = int(input(">"))
    if k == 1:
        print("Cool, my name is Van!\nCongratulation,have a nice day!")
        break
    else:
        print("Please try again")
