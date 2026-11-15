import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.advanced
def test_context_menu(driver):
    driver.get("https://the-internet.herokuapp.com/context_menu")
    actions = ActionChains(driver)
    box_below = driver.find_element(By.CSS_SELECTOR, "[id='hot-spot']")

    actions.context_click(box_below).perform()
    alert = driver.switch_to.alert

    assert alert.text == 'You selected a context menu'
    alert.accept()
