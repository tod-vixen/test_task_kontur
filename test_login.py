import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLoginFlow:
    """Набор тестов для проверки функционала входа и выхода из системы."""

    def test_incorrect_login_shows_error(self, driver, base_url):
        # 1. Переходим на главную страницу
        main_page = MainPage(driver)
        main_page.open(base_url)

        # 2. 🆕 Пытаемся закрыть баннер с куки (если он есть)
        main_page.handle_cookie_banner()

        # 3. Проверяем, что главная страница отображается корректно
        assert main_page.is_main_page_displayed(), "Главная страница не загрузилась"

        # 4. Переходим на страницу входа
        main_page.click_login_link()

        # 5. Вводим некорректные данные и нажимаем "Войти"
        login_page = LoginPage(driver)
        login_page.login("test", "test")

        # 6. Проверяем наличие сообщения об ошибке
        error_text = login_page.get_error_message().lower()
        assert any(
            word in error_text
            for word in ["неверн", "ошибк", "неправиль", "invalid", "error"]
        ), f"Сообщение об ошибке не найдено. Текст на странице: '{error_text}'"

    def test_successful_login_and_logout(
        self, driver, base_url, valid_username, valid_password
    ):
        # 1. Переходим на главную страницу
        main_page = MainPage(driver)
        main_page.open(base_url)

        # 2. 🆕 Пытаемся закрыть баннер с куки (если он есть)
        main_page.handle_cookie_banner()

        # 3. Проверяем, что главная страница отображается корректно
        assert main_page.is_main_page_displayed(), "Главная страница не загрузилась"

        # 4. Переходим на страницу входа
        main_page.click_login_link()

        # 5. Вводим корректные данные и входим
        login_page = LoginPage(driver)
        login_page.login(valid_username, valid_password)

        # 6. Проверяем, что нас перенаправило на главную страницу
        main_page.wait_for_url_to_contain(base_url)
        assert (
            main_page.is_main_page_displayed()
        ), "После входа главная страница не загрузилась"

        # 7. Кликаем на ссылку "Выход"
        main_page.click_logout_link()

        # 8. Проверяем, что мы вышли и вернулись на главную страницу
        main_page.wait_for_url_to_contain(base_url)
        assert (
            main_page.is_main_page_displayed()
        ), "После выхода главная страница не загрузилась"
