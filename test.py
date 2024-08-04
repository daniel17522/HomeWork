import colorama
import random
import colorama
from art import tprint
def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'algorithm']
    return random.choice(words)


def display_hangman(tries):
    print(colorama.Back.BLACK, colorama.Fore.YELLOW)
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        -----
        """
    ]
    return stages[tries]


def play_game():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    tprint(f"Давайте играть в Виселицу!", font="random")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Введите букву или слово целиком: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(colorama.Back.BLACK, colorama.Fore.BLUE)
                print(f"Вы уже угадывали букву {guess}.")
            elif guess not in word:
                print(colorama.Back.BLACK, colorama.Fore.RED)
                print(f"Буквы {guess} нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(colorama.Back.BLACK, colorama.Fore.GREEN)
                print(f"Отлично! Буква {guess} есть в слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"Вы уже угадывали слово {guess}.")
            elif guess != word:
                print(f"Слово {guess} не верно.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Некорректный ввод.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        tprint("You Win!", font="random")
    else:
        tprint(f"Game Over, слово было {word}", font="random")


if __name__ == "__main__":
    play_game()