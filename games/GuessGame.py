import utils
import random
import logging
from games.Game import Game



class GuessGame(Game):

    __secret_number = None
    __user_selection = None

    def __init__(self, difficulty):
        Game.__init__(self, difficulty)
        self.__secret_number = self.__generate_number()

    def __generate_number(self):
        num = random.randint(utils.MINIMUM_ALLOWED_NUM, self.get_difficulty())
        logging.debug(f"my secret number is {num}")
        return num

    def __get_guess_from_user(self):
        input_text = f"Please enter a number between {utils.MINIMUM_ALLOWED_NUM} and {self.get_difficulty()}: "
        return utils.get_num_input_in_range(input_text, utils.MINIMUM_ALLOWED_NUM, self.get_difficulty())

    def __compare_results(self):
        return utils.cmp(self.__secret_number, self.__user_selection)

    def play(self):
        self.__user_selection = self.__get_guess_from_user()
        print(f"Computer guess {self.__secret_number}. user guess {self.__user_selection}")
        # 1 -> False, 0 -> True, -1 -> True
        return self.__compare_results() != 1





