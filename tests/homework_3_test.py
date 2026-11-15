import pytest
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.advanced
def test_file_upload(driver):
    driver.get("https://the-internet.herokuapp.com/upload")
    file_path = Path("test_file.txt").resolve()

    upload_element = driver.find_element(By.CSS_SELECTOR, "[id='file-upload']")
    upload_element.send_keys(str(file_path))
    upload_button = driver.find_element(By.CSS_SELECTOR, "[id='file-submit']")
    upload_button.click()
    uploaded_files = (WebDriverWait(driver, 10)
     .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[id='uploaded-files']"))))

    assert uploaded_files.text == file_path.name
