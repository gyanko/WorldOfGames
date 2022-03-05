
class Game:
    __difficulty = None

    def __init__(self, difficulty):
        self.__difficulty = difficulty

    def get_difficulty(self):
        return self.__difficulty

