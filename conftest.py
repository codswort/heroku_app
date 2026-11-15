import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def download_driver():
    # Относительный путь, превращенный в абсолютный благодаря os.path.abspath
    download_dir = os.path.abspath("downloads")

    # makedirs - создает папку, exist_ok - чтобы не бросило ошибку FileExistsError, если существует
    os.makedirs(download_dir, exist_ok=True)

    options = Options()
    options.add_experimental_option("prefs", {  # chrome://settings
        "download.default_directory": download_dir,  # чтобы файлы сохранялись в нашу downloads, а не в системную
        "download.prompt_for_download": False,  # чтобы браузер не спрашивал «Сохранить как…»
        "download.directory_upgrade": True, # разрешает Chrome использовать указанную папку, даже если она была настроена в старой версии
        "safebrowsing.enabled": True,  # чтобы браузер не блокировал скачивание «подозрительных» файлов
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.download_dir = download_dir # сохраняет путь в атрибут, чтобы тест мог его прочитать

    yield driver
    driver.quit()