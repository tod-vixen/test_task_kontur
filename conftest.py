import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Загружаем секреты из файла .env
load_dotenv()


@pytest.fixture(scope="session")
def driver():
    """Настраивает и запускает браузер Chrome."""
    chrome_options = Options()

    # закомментируйте строку ниже знаком #. Иначе тесты будут работать в невидимом режиме.
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # 🆕 Добавляем настройки для автоматического принятия cookies и блокировки всплывающих окон
    prefs = {
        "profile.default_content_setting_values.cookies": 1,  # 1 = Разрешить cookies
        "profile.default_content_setting_values.notifications": 2,  # 2 = Блокировать уведомления
        "profile.default_content_setting_values.popups": 2,  # 2 = Блокировать всплывающие окна
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)  # Неявное ожидание элементов до 5 секунд

    yield driver  # Передаем драйвер в тесты

    driver.quit()  # Закрываем браузер после завершения всех тестов


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://100-dreley.ru/")


@pytest.fixture(scope="session")
def valid_username():
    return os.getenv("VALID_USERNAME", "test_user")


@pytest.fixture(scope="session")
def valid_password():
    return os.getenv("VALID_PASSWORD", "test_password")
