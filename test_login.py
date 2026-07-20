from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLoginFlow:
    
    def test_incorrect_login_shows_error(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open(base_url)
        
        # Закрываем куки, если они есть
        main_page.handle_cookie_banner()
        
        assert main_page.is_main_page_displayed(), "Главная страница не загрузилась"
        main_page.click_login_link()
        
        login_page = LoginPage(driver)
        login_page.login("test", "test")
        
        error_text = login_page.get_error_message().lower()
        assert any(word in error_text for word in
                   ["неверн", "ошибк", "неправиль", "invalid"]), \
            f"Сообщение об ошибке не найдено. Текст: '{error_text}'"
    
    def test_successful_login_and_logout(self, driver, base_url,
                                         valid_username, valid_password):
        main_page = MainPage(driver)
        main_page.open(base_url)
        
        # Закрываем куки, если они есть
        main_page.handle_cookie_banner()
        
        assert main_page.is_main_page_displayed(), "Главная страница не загрузилась"
        main_page.click_login_link()
        
        login_page = LoginPage(driver)
        login_page.login(valid_username, valid_password)
        
        main_page.wait_for_url_to_contain(base_url)
        assert main_page.is_main_page_displayed(), "После входа главная страница не загрузилась"
        
        main_page.click_logout_link()
        
        main_page.wait_for_url_to_contain(base_url)
        assert main_page.is_main_page_displayed(), "После выхода главная страница не загрузилась"
