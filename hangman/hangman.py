import random



print("HANGMAN")
print("The game will be available soon")
WORLDS = ["python", "java", "php", "javascript"]
play = True
while play:
    menu = input('Type "play" to play the game, "exit" to quit:\n  ')
    while menu not in ["play", "exit"]:
        menu = input('Type "play" to play the game')

