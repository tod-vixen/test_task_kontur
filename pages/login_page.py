from pages.base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):
    """Класс, описывающий действия на Странице входа."""
    
    def enter_username(self, username):
        self.send_keys(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def click_submit(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    def get_error_message(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)

    def login(self, username, password):
        """Удобный метод для выполнения полного процесса входа."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()