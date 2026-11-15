import pytest
from selenium.webdriver.common.by import By


@pytest.mark.advanced
def test_frames(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")
    iframe = driver.find_element(By.CSS_SELECTOR, "[id='mce_0_ifr']")
    driver.switch_to.frame(iframe)
    editor = driver.find_element(By.CSS_SELECTOR, "[data-id='mce_0']")

    assert editor.text == "Your content goes here.", "There should be the text 'Your content goes here.'!"
    driver.switch_to.default_content()
