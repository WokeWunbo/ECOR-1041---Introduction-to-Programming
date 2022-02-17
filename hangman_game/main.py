from os import remove
from random import randint

word_bank = None
file_name = "hangman_game\word_bank.json"

try:
    word_bank = open(file_name, "r")
except:
    print("couldn't find", file_name)
    
contents = word_bank.read()
word_list = contents.replace("[", "").replace("]", "").replace('"', "").split(",")
word_bank.close()

random_index = randint(0, len(word_list)-1)
word = word_list[random_index]

word_letters = list(word)
progress = [""] * len(word_letters)
max_tries = 6
tries = max_tries

while (str(progress) != str(word_letters)) and tries > 0:
    guessed_letter = input("Guess a letter: ")
    guessed_correct = False
    for i in range(0, len(word_letters)):
        letter = word_letters[i]
        if guessed_letter == letter:
            progress[i] = guessed_letter
            guessed_correct = True
    if not guessed_correct: 
        tries -= 1
        print("\nWRONG!", tries, "left.")

if not (str(progress) != str(word_letters)) and tries > 0:
    print("\nYOU WON")
else:
    print("\nYou lost")