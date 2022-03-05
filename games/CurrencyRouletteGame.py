import utils
import random
import logging
from handlers.free_currency_api_handler import get_currency_rate
from games.Game import Game
# This game will use the free currency api to get the current exchange rate from USD to ILS, will

class CurrencyRouletteGame(Game):

    __comp_money_usd = None
    __usd_ils_exchange_rate = None

    def __init__(self, difficulty):
        Game.__init__(self, difficulty)
        self.__comp_money_usd = random.randint(utils.MINIMUM_ALLOWED_NUM, utils.CURRENCY_ROULETTE_MAX_ALLOWED_NUM)
        self.__usd_ils_exchange_rate = get_currency_rate("ILS")
        logging.debug(f"I have selected {self.__comp_money_usd} usd, with exchange rate {self.__usd_ils_exchange_rate}")


    def __get_money_interval(self):
        comp_money_in_ils = self.__comp_money_usd * self.__usd_ils_exchange_rate
        interval_window = (5 - self.get_difficulty())
        min_interval = round(comp_money_in_ils - interval_window, 2)
        max_interval = round(comp_money_in_ils + interval_window, 2)
        logging.debug(f"my intervals are {min_interval} and {max_interval}")
        return min_interval, max_interval


    def __get_guess_from_user(self):
        text = f"Try and guess {self.__comp_money_usd}$ in ILS: "
        self.__user_guess_in_ils = utils.get_float_input(text)
        logging.debug(f"user guess is {self.__user_guess_in_ils}")


    def play(self):
        self.__get_guess_from_user()
        interval_min, interval_max = self.__get_money_interval()
        print(f"computer selected a sum between {interval_min:.2f} and {interval_max:.2f}. you chose {self.__user_guess_in_ils}.")
        return interval_min <= self.__user_guess_in_ils <= interval_max
