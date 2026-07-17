import os
import pytest
import allure
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless=new") # Раскомментируй для безголового режима
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# --- Хуки для Allure ---

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Автоматически прикрепляет скриншот к отчету Allure, если тест завершился с ошибкой (failed).
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Проверяем, что это фаза вызова (call) и тест упал
    if rep.when == "call" and rep.failed:
        # Получаем экземпляр драйвера из фикстур теста
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Скриншот при падении теста",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")

def pytest_sessionstart(session):
    """
    Добавляет информацию об окружении в начало отчета Allure.
    """
    allure.environment(browser="Google Chrome")
    allure.environment(python_version=os.sys.version.split()[0])
    allure.environment(test_env="Linux.Org.Ru Staging/Prod")