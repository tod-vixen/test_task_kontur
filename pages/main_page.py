from pages.base_page import BasePage
from locators import MainPageLocators, CookieBannerLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)


class MainPage(BasePage):
    """Класс, описывающий действия на Главной странице."""

    def is_main_page_displayed(self):
        """Проверяет, что главная страница успешно загрузилась."""
        return bool(self.find_element(MainPageLocators.MAIN_PAGE_INDICATOR))

    def handle_cookie_banner(self):
        """
        Пытается нажать кнопку 'Принять' в баннере cookies.
        Если баннера нет или кнопка не нажимается, метод просто завершается, не ломая тест.
        """
        try:
            # Ждем появления кнопки максимум 3 секунды
            button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(CookieBannerLocators.ACCEPT_BUTTON)
            )
            button.click()
        except (TimeoutException, ElementClickInterceptedException):
            # Если кнопка не появилась или перекрыта чем-то еще, пробуем "хак" через JavaScript
            try:
                banner = self.driver.find_element(
                    *CookieBannerLocators.BANNER_CONTAINER
                )
                self.driver.execute_script(
                    "arguments[0].style.display = 'none';", banner
                )
            except Exception:
                # Если и баннера нет, просто игнорируем и идем дальше. Это нормально.
                pass

    def click_login_link(self):
        """Кликает на ссылку 'Вход'."""
        self.click(MainPageLocators.LOGIN_LINK)

    def click_logout_link(self):
        """Кликает на ссылку 'Выход'."""
        self.click(MainPageLocators.LOGOUT_LINK)
