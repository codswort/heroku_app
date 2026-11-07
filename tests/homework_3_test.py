import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.basic
def test_dropdown(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = browser.find_element(By.ID, "dropdown")

    select = Select(dropdown)
    options = select.options

    assert len(options) == 3, "There should be 3 options"

    select.select_by_index(1)
    assert options[1].is_selected(), "There should be selected 1 option"

    select.select_by_index(2)
    assert options[2].is_selected(), "There should be selected 2 option"
