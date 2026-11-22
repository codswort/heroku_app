import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.advanced
def test_frames(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")
    iframe = driver.find_element(By.CSS_SELECTOR, "[id='mce_0_ifr']")
    driver.switch_to.frame(iframe)
    try:
        editor = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-id='mce_0'] p"))
        )

        assert editor.text == "Your content goes here.", "There should be the text 'Your content goes here.'!"
    finally:
        driver.switch_to.default_content()
