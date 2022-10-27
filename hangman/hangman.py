import random

print("HANGMAN")
print("The game will be available soon.")
WORLDS = ["python", "java", "php", "javascript"]
play = True
while play:
    menu = input('Type "play" to play the game, "exit" to quit:\n>')
    while menu not in ["play", "exit"]:
        menu = input('Type "play" to play the game, "exit" to quit:\n>')
    if menu == "play":
        word = random.choice(WORLDS)
        remember_letters = []
        input_letters = []
        all_letters = list(set(word))
        words = "".join([i if i in remember_letters else "" for i in word])
        print(words)
        life = 8
        while life > 0:
            letter = input("Input a letter:")
            if letter == letter.lower() and len(letter) == 1:
                if letter in word and letter not in remember_letters and letter not in input_letters:
                    remember_letters.append(letter)
                    all_letters.remove(letter)
                elif letter in remember_letters or letter in input_letters:
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    life -= 1