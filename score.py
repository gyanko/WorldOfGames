from utils import SCORES_FILE_NAME, SCORES_BONUS, SCORES_DIFFICULTY_FACTOR
import json
import os
import logging


class Score():
    _username = None

    def __init__(self, username):
        self._username = username

    @staticmethod
    def get_scores_dict():
        scores_dict = {}
        with open(SCORES_FILE_NAME, 'a+') as scores_handle:  # append or read
            scores_handle.seek(0)
            if os.stat(SCORES_FILE_NAME).st_size > 0:  # check empty file
                scores_dict = json.load(scores_handle)
        return scores_dict

    def _save_scores_dict(self, scores_dict):
        with open(SCORES_FILE_NAME, 'w') as scores_handle:
            json.dump(scores_dict, scores_handle)

    def add_score(self, difficulty):
        registered_high_scores = self.get_scores_dict()
        logging.debug(f"system high scores: {registered_high_scores}")
        current_score = (difficulty * SCORES_DIFFICULTY_FACTOR) + SCORES_BONUS
        logging.debug(f"current user score is {current_score}")
        # print(f"calc score {current_score}")
        user_high_score = registered_high_scores.get(self._username)
        logging.debug(f"user {self._username} saved high score is {user_high_score}")
        # if no high score for user or current score is larger than saved high score
        if (user_high_score is None) or (current_score > user_high_score):
            logging.debug("updating high scores...")
            registered_high_scores[self._username] = current_score
            self._save_scores_dict(registered_high_scores)



