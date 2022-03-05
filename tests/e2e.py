from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import logging
import sys
import traceback

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_dir)
from utils import FLASK_IP_BIND, FLASK_PORT_BIND
from utils import GOOD_RETURN_CODE, BAD_RETURN_CODE


def test_scores_service(uri):
    return_code = GOOD_RETURN_CODE
    try:
        drv_file = os.path.join(os.path.dirname(__file__), 'chromedriver')
        driver = webdriver.Chrome(executable_path=drv_file)
        driver.get(uri)
        scores = driver.find_elements(By.XPATH, "//*[contains(@id, 'score_')]")
        for score in scores:
            if not (score.text.isnumeric() and 0 <= int(score.text) <= 100):
                return_code = BAD_RETURN_CODE
    except:
        traceback.print_exc()
        return_code = BAD_RETURN_CODE
    finally:
        driver.close()
    return return_code


def main_function(test_uri):
    exit_code = test_scores_service(test_uri)
    logging.log(0, f"scoring module testing exit code {exit_code}")
    assert exit_code == GOOD_RETURN_CODE


uri = f"http://{FLASK_IP_BIND}:{FLASK_PORT_BIND}"
if len(sys.argv) > 1 and sys.argv[1]:
    uri = sys.argv[1]
print(f"testing address {uri}")
main_function(uri)
