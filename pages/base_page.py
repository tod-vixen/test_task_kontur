from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс для всех страниц. Содержит универсальные действия."""
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
    
    def open(self, url):
        """Открывает переданный URL в браузере."""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Находит элемент и ждет его появления на странице до timeout секунд."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def click(self, locator):
        """Находит элемент и кликает по нему."""
        element = self.find_element(locator)
        element.click()
    
    def send_keys(self, locator, text):
        """Находит поле ввода, очищает его и вводит текст."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Возвращает текстовое содержимое элемента."""
        return self.find_element(locator).text
    
    def wait_for_url_to_contain(self, text, timeout=10):
        """Ждет, пока адрес страницы (URL) начнет содержать указанную строку."""
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
