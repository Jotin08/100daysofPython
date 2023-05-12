import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}.")
    else:
        found = False
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                found = True

        if not found:
            print(f"You've guessed {guess}. That is not the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}.")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
