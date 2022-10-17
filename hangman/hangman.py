import random



print("HANGMAN")
print("The game will be available soon")
WORLDS = ["python", "java", "php", "javascript"]
play = True
while play:
    menu = input('Type "play" to play the game, "exit" to quit:\n  ')
    while menu not in ["play", "exit"]:
        menu = input('Type "play" to play the game, "exit" to quit:\n')
    if menu == "play":
        word = random.choice(WORLDS)
        remember_letters = []
        input_letters = []
        all_letters = list(set(word))
        words = "" .join([i if i in remember_letters else "" for i in word])
        print(words)
        live = 8
        while live > 0:
            letter = input("Input a letter:")


