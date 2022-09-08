from hangman_art import stages, logo
from hangman_words import word_list
import random 
print(logo)
chosen_word = random.choice(word_list)
# print(f"The chosen word is {chosen_word}")
lives = 6
display = [] # displays the blanks and correctly guessed letters
for letter in chosen_word:
    display.append("_")
game_finished = False
guessed = [] # tracks guessed letters
while not game_finished:
    # validating guess
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("You have already guessed this letter. Try another one")
        continue
    elif len(guess) > 1:
        print("Only guess one letter.")
        continue
    else:
        guessed.append(guess)

    # decrementing lives
    if guess not in chosen_word:
        lives -= 1
        print(f"You now have {lives} lives.")
    
        if lives == 0:
            game_finished = True
            print("You lose")
            print(f"The correct word is {chosen_word}.")

    # placing letters in display
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(' '.join(display))

    # checking if game over
    if "_" not in display:
        game_finished = True
        print("You Won! ")
    print(stages[lives])
