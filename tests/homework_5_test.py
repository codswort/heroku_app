import os
import time
import pytest

from selenium.webdriver.common.by import By


def wait_for_download(download_dir, filename, timeout=30):
    target = os.path.join(download_dir, filename)
    crdownload = target + ".crdownload"
    end_time = time.time() + timeout

    while time.time() < end_time:
        # Chrome удаляет .crdownload только после успешного завершения
        if os.path.exists(target) and not os.path.exists(crdownload):
            time.sleep(0.3)  # защита от гонки записи на диск
            if os.path.exists(target) and os.path.getsize(target) > 0:
                return target
        time.sleep(0.5)

    raise TimeoutError(
        f"Файл {filename!r} не появился за {timeout}с. "
        f"В {download_dir}: {os.listdir(download_dir)}"
    )

@pytest.mark.advanced
def test_file_download(download_driver):
    download_driver.get("https://the-internet.herokuapp.com/download")
    upload_element = download_driver.find_element(By.CSS_SELECTOR, "[href='download/test_upload.txt']")
    upload_element.click()

    file_path = wait_for_download(download_driver.download_dir, upload_element.text)
    assert os.path.getsize(file_path) > 0, "There should be no file downloaded."
