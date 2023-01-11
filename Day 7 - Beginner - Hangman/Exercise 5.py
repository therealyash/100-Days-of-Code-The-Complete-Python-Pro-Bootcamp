# Step 4
import random
import hangman_art
import hangman_words
stages = hangman_art.stages




len_stages = len(stages)

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

# Testing code

print(hangman_art.logo)
print('WELCOME TO HANGMAN!')
#print(f'Pssst, the solution is {chosen_word}.')

# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
len_chosen_word = len(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display += "_"
print("".join(display))
print(f"Hint: The word is of {len_chosen_word} letters.")

# guess = input("Guess a letter: ").lower()
#
# for i in range(len_chosen_word):
#     if chosen_word[i] == guess:
#         display[i] = chosen_word[i]
#     else:
#         pass
# print(display)

# TODO-1: - Use a while loop to let the user guess again. The loop
# should only stop once the user has guessed all the letters in the
# chosen_word and 'display' has no more blanks ("_"). Then you can
# tell the user they've won.
#print(stages[len_stages-1])
while '_' in display:
    guess = input("Guess a letter: ").lower()
    for i in range(len_chosen_word):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
        else:
            pass
    print("".join(display))

    if guess not in display:
        if len_stages < 1:
            print('Than man is Hanged! Game Over!')
            print(f'The word was {chosen_word}!')
            print('Well Tried!')
            break
        else:
            len_stages -= 1
            print(f'You guessed {guess}, that is not in the word! You lose a life')
            print(stages[len_stages])

else:
    print('You Win! Game Over!')