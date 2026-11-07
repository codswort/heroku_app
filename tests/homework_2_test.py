import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_checkboxes(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")

    assert not checkboxes[0].is_selected()
    checkboxes[0].click()
    assert checkboxes[0].is_selected()

    assert checkboxes[1].is_selected()
    checkboxes[1].click()
    assert not checkboxes[1].is_selected()
