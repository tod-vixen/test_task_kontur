from selenium.common.exceptions import TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import MainPageLocators, CookieBannerLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Класс, описывающий действия на Главной странице."""
    
    def is_main_page_displayed(self):
        """Проверяет, что главная страница успешно загрузилась."""
        return bool(self.find_element(MainPageLocators.MAIN_PAGE_INDICATOR))
    
    def handle_cookie_banner(self):
        """
        Пытается нажать кнопку 'Принять' в баннере cookies.
        Если баннера нет, метод молча завершается, не ломая тест.
        """
        try:
            # Ждем появления кнопки максимум 3 секунды
            button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(CookieBannerLocators.ACCEPT_BUTTON)
            )
            button.click()
        except (TimeoutException, ElementClickInterceptedException):
            # Если кнопка не появилась или перекрыта, игнорируем. Это нормально.
            pass
    
    def click_login_link(self):
        """Кликает на ссылку 'Вход'."""
        self.click(MainPageLocators.LOGIN_LINK)
    
    def click_logout_link(self):
        """Кликает на ссылку 'Выход'."""
        self.click(MainPageLocators.LOGOUT_LINK)
