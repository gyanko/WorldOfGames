from Live import load_game, welcome
from utils import LOG_LEVEL
import logging

# set logging
logging.basicConfig(level=LOG_LEVEL)

name = input("please enter your name:")
print(welcome(name))
load_game(name)
