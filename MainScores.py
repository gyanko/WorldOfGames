from utils import SCORES_TEMPLATE,FLASK_ERROR_TEMPLATE
from utils import FLASK_IP_BIND, FLASK_PORT_BIND, FLASK_TEMPLATE_FOLDER
from flask import Flask, render_template
from score import Score
import logging


def get_scores():
    try:
        score = Score.get_scores_dict()
        data = render_template(SCORES_TEMPLATE, scores=score)
    except Exception as e:
        data = render_template(FLASK_ERROR_TEMPLATE, error=e)
    return data


def score_server():
    # log = logging.getLogger('werkzeug').disabled = True

    app = Flask('app', template_folder=FLASK_TEMPLATE_FOLDER)
    app.add_url_rule(rule="/", view_func=get_scores, methods=["GET"])
    logging.debug(f"starting server on {FLASK_IP_BIND}:{FLASK_PORT_BIND}...")
    app.run(host=FLASK_IP_BIND, port=FLASK_PORT_BIND, debug=True)


score_server()

