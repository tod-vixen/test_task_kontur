import os
import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

@allure.epic("Аутентификация на Linux.Org.Ru")
@allure.feature("Управление сессией пользователя")
class TestAuth:

    @allure.title("Проверка корректной загрузки главной страницы")
    @allure.description("Тест проверяет, что главная страница открывается и заголовок содержит 'Linux.Org.Ru'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_loads(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.is_title_correct(), "Заголовок главной страницы не соответствует ожидаемому"

    @allure.title("Проверка отображения ошибки при некорректных данных")
    @allure.description("Тест вводит заведомо неверные логин и пароль и проверяет наличие сообщения об ошибке")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        login_page = main_page.go_to_login_page()
        
        login_page.login("test_invalid_user", "test_invalid_password")
        
        error_msg = login_page.get_error_message()
        assert error_msg, "Сообщение об ошибке не отображается при неверных данных"
        assert "неправильн" in error_msg.lower() or "неверн" in error_msg.lower() or "ошибка" in error_msg.lower(), \
            f"Текст ошибки не соответствует ожидаемому. Получено: '{error_msg}'"

    @allure.title("Проверка успешного входа и выхода из системы")
    @allure.description("Тест использует реальные учетные данные из .env для входа, проверяет наличие кнопки 'Выход', выполняет выход и проверяет возврат на главную")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skipif(
        not (os.getenv("LOR_USERNAME") and os.getenv("LOR_PASSWORD")), 
        reason="Учетные данные не найдены. Проверьте наличие и заполнение файла .env (LOR_USERNAME и LOR_PASSWORD)."
    )
    def test_valid_login_and_logout(self, driver):
        username = os.getenv("LOR_USERNAME")
        password = os.getenv("LOR_PASSWORD")
        
        main_page = MainPage(driver)
        main_page.open()
        
        login_page = main_page.go_to_login_page()
        login_page.login(username, password)
        
        assert main_page.is_logged_in(), "Пользователь не вошел в систему. Кнопка 'Выход' не найдена."
        
        main_page.logout()
        
        assert main_page.is_logged_out(), "Пользователь не вышел из системы. Кнопка 'Вход' не найдена."
        assert main_page.is_title_correct(), "После выхода перенаправление на главную страницу не произошло."