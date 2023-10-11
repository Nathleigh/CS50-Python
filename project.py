# ASCIIdle
# Harvard CS50 Python final project - Nathan Chapman, 2023

# Your project must have a main function and three or more additional functions.
# At least three of those additional functions must be accompanied by tests that
# can be executed with pytest.
# Your main function must be in a file called project.py, which should be in the
# “root” (i.e., top-level folder) of your project.
# Your 3 required custom functions other than main must also be in project.py
# and defined at the same indentation level as main (i.e., not nested under any
# classes or functions).

import random
import os


def main():
    '''Main function for ASCIIdle puzzle game.
    '''
    if os.name == 'posix':  # Linux and macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    print("Welcome to ASCIIdle :) Guess the word in 6 tries or less to win!")
    while True:
        word_length = int(input("Choose word length (number of letters, between 2 and 21): "))
        if word_length < 2 or word_length > 21:
            continue
        else:
            break
    answer, dict_file = get_answer(word_length)

    # Codes to set background colour for text feedback
    bright_green = '\u001b[42;1m'
    bright_yellow = '\u001b[43;1m'
    red = '\u001b[41m'
    reset = '\u001b[0m'
    print("Each guess will be shown with coloured feedback for each letter.")
    print(f'{bright_green}A{reset} indicates the correct letter and position.')
    print(f'{bright_yellow}B{reset} means the letter is in the word, but in the wrong position.')
    print(f'{red}C{reset} means that the letter is not in the word.\n')
    # print("ANSWER = ", answer)  # for debugging purposes
    print("Start!", end="")
    # Give user 6 attempts to guess the answer word
    for i in range(1,7):
        guess = get_guess(word_length, dict_file)
        check_guess(guess, answer)
        if guess == answer:
            print(" - CORRECT!!!")
            print(f"You won in {i} tries.")
            exit()
    print()
    print(f"You lost. The answer was {answer.upper()}.")


def get_answer(chosen_length):
    '''Opens the text file words.txt and reads the contents into a dictionary,
    then randomly selects a word of chosen_length.
    Input argument: chosen_length (int)
    Returns: answer (string) and dict_file (dictionary)'''
    dict_file = {}
    with open("words.txt") as f:
        for line in f:
            w = line.strip()
            length = len(w)
            dict_file.setdefault(length, []).append(w)
    answer = random.choice(dict_file[chosen_length])
    return answer, dict_file


def get_guess(length, dict_file):
    '''This function prompts the user to guess a word and verifies that
    the word length matches the answer, and that the guess is a valid word.
    Input args: length (int), dict_file (dictionary)'''
    while True:
        guess = input(" - Type in your guess: ").strip().lower()
        if len(guess) != length:
            print(f"Your guess must have {length} letters!", end='')
        else:
            if guess in dict_file[length]:
                return guess
            print("That's not a valid word", end='')
            continue


def check_guess(guess, answer):
    '''This function iterates through the letters in the user's guess and
    prints out colour-coded feedback for each letter.
    Input args: guess (string, answer (string)'''

    # Codes to set background colour for text feedback
    green = '\u001b[42m'
    bright_green = '\u001b[42;1m'
    yellow = '\u001b[43m'
    bright_yellow = '\u001b[43;1m'
    red = '\u001b[41m'
    bright_red = '\u001b[41;1m'
    reset = '\u001b[0m'

    answer_letter_list = list(answer)
    # print("answer_letter_list:", answer_letter_list)

    # Create empty list, with one element per letter in the answer word
    # initially assume all are incorrect
    # Create list to store the color-coded letters for each position
    colored_letters = ["_"] * len(answer)
    # print("colored_letters, empty:", colored_letters)

    # Iterate through each letter in the guess
    # First pass: check for characters definitely right or wrong
    for i, letter in enumerate(guess):
        # Correct letter and correct position
        if letter == answer[i]:
            colored_letters[i] = f"{bright_green}{letter.upper()}{reset}"
            answer_letter_list.remove(letter)
        # For letters which do not occur anywhere in the answer
        elif letter not in answer:
            colored_letters[i] = f"{red}{letter.upper()}{reset}"

    # Second pass: check for correct letter in wrong place
    for i, letter in enumerate(guess):
        if colored_letters[i] == '_':
            if letter in answer_letter_list:
                # Correct letter but wrong position
                colored_letters[i] = f"{bright_yellow}{letter.upper()}{reset}"
                answer_letter_list.remove(letter)
            else:
                colored_letters[i] = f"{red}{letter.upper()}{reset}"

    # Print the colored letters
    print("".join(colored_letters), end='')


if __name__ == "__main__":
    main()

