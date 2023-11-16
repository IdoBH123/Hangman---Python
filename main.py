
from hangman_picture import print_hangman

# import other libraries functions (requires installing them)
from colorama import Fore, Back, Style


from termcolor import colored

NOT_UPDATED_STR = "\n{0}"
MAX_TRIES = 7


def check_win(secret_word, old_letters_guessed):
    """"
    this function will check if the secret word was already guessed by the letters
    :param: secret_word: string of the secret world
    :param:old_letters_guessed: lis of all the letters was guessed already
    :type: string
    :type: list
    :return: the answer if the word was discovered
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """"
    this function will place the old ldtters in the right place if its contain in the secret word
    :param: secret_word: string of the secret world
    :param:old_letters_guessed: lis of all the letters was guessed already
    :type: string
    :type: list
    :return: string partially disclosing the secret word and underlines in the gaps
    :rtype: str
    """
    out_str = ""
    for secret_char in secret_word:
        if secret_char in old_letters_guessed:
            out_str += secret_char + " "
        else:
            out_str += "_ "
    return out_str[:-1]


def check_valid_input(letter_guessed, old_letters_guessed):
    """"
    the function will check if the letter was checked already or contaion over
    than 1 char or is alpha element
    :param letter_guessed: char was guessed
    :param old_letters_guessed: list of already char chcked
    :type letter_guessed : char
    :type old_letters_guessed : list
    :return: the answer of all the check's
    :rtype:bool
    """
    letter_guessed = letter_guessed.lower()
    check1 = len(letter_guessed) > 1  ## checking the len of the letter guessed is better than 1
    check2 = letter_guessed.isalpha()  ## check of the letter guessed is alpha
    check3 = letter_guessed in old_letters_guessed  ## check if the letter is new or chcked already

    if check1 or (not check2) or check3:
        return 0
    else:
        return 1


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """"
    this function will check if the letter is valid and if yes will add it to the
    old letters list, else will change the list to string and change the "," to "->"
    :param letter_guessed: char was guessed
    :param old_letters_guessed: list of already char chcked
    :type letter_guessed : char
    :type old_letters_guessed : list
    :return: the answer of all the check's
    :rtype:bool
    """
    letter_guessed = letter_guessed.lower()
    valid_input = check_valid_input(letter_guessed, old_letters_guessed)
    if valid_input == 1:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print_list_not_updated(old_letters_guessed)
        return False


def print_list_not_updated(my_list):
    """Prints not-updated string
    :param my_list (not updates)
    :type my_list: list
    """
    print(NOT_UPDATED_STR.format(" -> ".join(sorted(my_list))))


def choose_word(file_path, index):
    """Picks one word from a list of words, read from a file, according to a given index in the list
    :param: file_path: the path of the file that contains a word list
    :param: index: the position of the word to be picked
    :type: file_path: string
    :type: index: int
    :return: number of distinct words in the list and the picked word
    :rtype: tuple
    """
    str_words = ""
    with open(file_path, "r") as input_file:
        words_list = [line.rstrip() for line in input_file]  # option for word per line
        ##str_words = input_file.readlines()   # option for long list words
    ##list_words = list(str_words.split(" "))
    if len(words_list) < index - 1:
        calc = index % len(words_list)
        hide_word = words_list[calc - 1]

    else:
        hide_word = words_list[index - 1]  # the word need to guess

    return hide_word


def main():
    # this path for the welcome screen need to change it according to your path document
    with open(r'C:\Users\עידו בן הרוש\PycharmProjects\pythonProject\welcome_screen.txt', "r") as welcome_file:
        print(welcome_file.read())

    # the text file path, contains english word list separated by spaces
    text_file_path = input("Enter file path: ")

    # int rep the idx of word in the file
    index_str = int(input("Enter index: "))

    ##secret_word_index = int(index_str)

    secret_word = choose_word(text_file_path, index_str)

    # the letters that the player guessed already
    old_letters_guessed = list()

    num_of_tries = 1

    while num_of_tries <= MAX_TRIES:
        hangman_picture_screen = print_hangman(num_of_tries)

        if num_of_tries == MAX_TRIES:
            print(Fore.RED+Back.BLACK+"You lose the game :(  ")
            break

        hidden_word = show_hidden_word(secret_word, old_letters_guessed)
        print(hidden_word)

        if check_win(secret_word, old_letters_guessed):
            print(Fore.LIGHTBLUE_EX+Back.GREEN+"You Are King - did it!!! ")
            break

        # The player will guess the letter
        while True:
            guess_letter_input = input("Guess a letter: ")
            is_valid = try_update_letter_guessed(guess_letter_input, old_letters_guessed)
            if not is_valid: ##if the letter in invalid
                print("X - Invalid_letter ")
                continue
            elif guess_letter_input.lower() not in secret_word: ## if the letter is valid but incorrect
                print("NO - Guess new letter")
                num_of_tries += 1
                break
            else: ## if the secret word contain the guess
                print("YEAAAA continue guessing")
                break


    ##print(choose_word(r'c:\words.txt',5))

if __name__ == "__main__":
    main()