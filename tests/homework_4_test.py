import time
import pytest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_inputs(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")
    input_field = browser.find_element(By.TAG_NAME, "input")

    input_field.send_keys("A")
    assert input_field.get_attribute("value") == "", "The input field should be empty"

    input_field.send_keys("1e2")
    time.sleep(1)
    assert input_field.get_attribute("value") == "1e2", "The input field should be = 1e2"

    input_field.clear()
    input_field.send_keys("45")
    time.sleep(1)
    assert input_field.get_attribute("value") == "45", "The input field should be = 45"

    input_field.send_keys(Keys.ARROW_UP)
    time.sleep(1)
    assert input_field.get_attribute("value") == "46", "The input field should be = 46"

    input_field.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    assert input_field.get_attribute("value") == "45", "The input field should be = 45"
