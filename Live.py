from utils import get_num_input_in_range, MINIMUM_ALLOWED_NUM, MAX_DIFFICULTY
from score import Score
from games.MemoryGame import MemoryGame
from games.CurrencyRouletteGame import CurrencyRouletteGame
from games.GuessGame import GuessGame


def welcome(name):
    welcome_msg = f"""Hello {name} and welcome to the World of Games (WoG)
Here you can find many cool games to play
"""
    return welcome_msg


def load_game(username):
    game_menu = """Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
Enter your selection: """
    diff_menu = """Please choose game difficulty from 1 to 5:"""
    games = {'1': MemoryGame, '2': GuessGame, '3': CurrencyRouletteGame}

    game_selection = get_num_input_in_range(game_menu, MINIMUM_ALLOWED_NUM, len(games))
    diff_selection = get_num_input_in_range(diff_menu, MINIMUM_ALLOWED_NUM, MAX_DIFFICULTY)

    game = games[str(game_selection)](diff_selection)

    user_is_winner = game.play()
    user_title = 'WINNER' if user_is_winner else 'LOSER'
    print(f"You are a {user_title}. Good Bye")

    if user_is_winner:
        Score(username).add_score(diff_selection)





