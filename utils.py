import os
import logging

# flask server consts
FLASK_IP_BIND = "0.0.0.0"
FLASK_PORT_BIND = "4000"
FLASK_ERROR_TEMPLATE = "errorView.html"
FLASK_TEMPLATE_FOLDER = "resources"

# general consts
MINIMUM_ALLOWED_NUM = 1
MAX_DIFFICULTY = 5
BAD_RETURN_CODE = -1
GOOD_RETURN_CODE = 0
LOG_LEVEL = logging.INFO

# memory game
MEMORY_GAME_MAX_ALLOWED_NUM = 101
MEMORY_GAME_SLEEP_TIME_SECS = 0.7

# currency roulette
CURRENCY_ROULETTE_MAX_ALLOWED_NUM = 100

# scores
SCORES_FILE_NAME = "scores.txt"
SCORES_DIFFICULTY_FACTOR = 3
SCORES_BONUS = 5
SCORES_TEMPLATE = "scoreView.html"

# handlers
# Free Currency
FREE_CURRENCY_URI = 'https://freecurrencyapi.net/api/v2/latest?apikey=80e4c990-64ba-11ec-a0db-433f7c105da7'


# generic function to receive valid int from user within min and max value provided.
def get_num_input_in_range(input_text, min_value, max_value):
    valid_input = False
    result = None
    while not valid_input:
        some_input = input(input_text)
        # user selection is not a number
        if not some_input.isnumeric():
            print(f"your input {some_input} is not a valid number. Please type again")
            continue
        some_input = int(some_input)
        if not min_value <= some_input <= max_value:
            print(f"valid inputs are between {min_value} and {max_value}. Please type again.")
            continue
        valid_input = True
    return some_input


def get_float_input(input_text):
    valid_input = False
    result = None
    while not valid_input:
        some_input = input(input_text)
        # user selection is not a number
        try:
            some_input = float(some_input)
            valid_input = True
        except ValueError:
            print(f"your input {some_input} is not a valid number. Please choose again")
    return some_input


# comparison between two ints
def cmp(a, b):
    return (a > b) - (a < b)


def screen_cleaner():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
