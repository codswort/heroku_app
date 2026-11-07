import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_typos(browser):
    browser.get("https://the-internet.herokuapp.com/typos")
    right_text = "Sometimes you'll see a typo, other times you won't."

    for i in range(1, 10):
        input_field = browser.find_elements(By.TAG_NAME, "p")
        paragraph = input_field[1].text
        if paragraph == right_text:
            assert paragraph == right_text
            break
        else:
            assert not paragraph == right_text
        browser.refresh()
