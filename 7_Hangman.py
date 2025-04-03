import random

logo = """
     _   _                                         
    | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    |  _  | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        | |                      
                        |_|                      
    """

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]

print(logo)

lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for i in range(word_length):
    placeholder += "_"

print("\nWord to guess: " + placeholder)

game_over = False

correct_letters = []

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in correct_letters:
        print(f"\nyou've already guessed the letter {guess}")

    display = ""

    for letter in chosen_word:
        if letter==guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou guessed the letter {guess}, that's not in the word. You lose a life.")
        print(f"******** {lives}/6 lives left ********")

        if lives==0:
            game_over = True

            print(f"\n******** It was {chosen_word}! You Lose ********")

    if "_" not in display:
        game_over = True
        print("\n******** You Win ********")
        print(f"******** The word is {chosen_word} ********")

    print(stages[6-lives])