from colorama import Fore, Back, Style

HANGMAN_PHOTOS = {
    1: "    x-------x",
    2: """    x-------x
    |
    |
    |
    |
    |""",
    3: """    x-------x
    |       |
    |       0
    |
    |
    |""",
    4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
    5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
    6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""",
}


def print_hangman(num_of_tries):
    """Prints hangman state, according to input nunmer with some colors.
    :param: num_of_tries: define the state to be displayed
    :type: int
    """
    if num_of_tries == 1:
        print(Fore.BLUE+HANGMAN_PHOTOS[num_of_tries])
    elif num_of_tries == 2:
        print(Fore.LIGHTBLUE_EX + HANGMAN_PHOTOS[num_of_tries])
    elif num_of_tries == 3:
        print(Fore.CYAN + HANGMAN_PHOTOS[num_of_tries])
    elif num_of_tries == 4:
        print(Fore.LIGHTMAGENTA_EX + HANGMAN_PHOTOS[num_of_tries])
    elif num_of_tries == 5:
        print(Fore.LIGHTYELLOW_EX + HANGMAN_PHOTOS[num_of_tries])
    elif num_of_tries == 6:
        print(Fore.LIGHTRED_EX + HANGMAN_PHOTOS[num_of_tries])
    else:
        print(Fore.RED + HANGMAN_PHOTOS[num_of_tries])


        #print(HANGMAN_PHOTOS[num_of_tries])



