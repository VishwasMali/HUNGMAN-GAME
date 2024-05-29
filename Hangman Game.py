import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon","dragonfruit","mango","kiwi","pineapple","jackfruit","lemon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. {attempts} attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word)
                break
        else:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break

if __name__ == "__main__":
    hangman()
