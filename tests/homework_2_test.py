import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.advanced
def test_dynamic_controls(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    remove_button = driver.find_element(By.CSS_SELECTOR, "[onclick='swapCheckbox()']")
    remove_button.click()
    waitting = (WebDriverWait(driver, 10)
                .until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id='message']"),"It's gone!")))
    assert waitting, "There should be text = It's gone!"

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    assert len(checkboxes) == 0, "There should be length = 0"

    input_field = driver.find_element(By.CSS_SELECTOR, "[type='text']")
    assert not input_field.is_enabled(), "There should be not enabled input field"

    enable_button = driver.find_element(By.CSS_SELECTOR, "[onclick='swapInput()']")
    enable_button.click()
    (WebDriverWait(driver, 10)
     .until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id='message']"), "It's enabled!")))

    assert input_field.is_enabled(), "There should be enabled input field"
