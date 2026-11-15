import pytest
from selenium.webdriver.common.by import By


@pytest.mark.advanced
def test_add_remove_elements(driver):
    driver.get("https://the-internet.herokuapp.com/context_menu/")
    actions = ActionChains(driver)
    add_element = driver.find_element(By.XPATH, "//button[text()='Add Element']")

    add_element.click()
    add_element.click()

    delete_elements = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    assert len(delete_elements) == 2, "There should be 2 elements"
