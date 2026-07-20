from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для Главной страницы."""
    # Ссылка на вход
    LOGIN_LINK = (By.CSS_SELECTOR, ".account_link[href='user/login']")
    
    # Ссылка на выход (появляется после авторизации)
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='user/logout']")
    
    # Индикатор загрузки страницы (медленный элемент)
    MAIN_PAGE_INDICATOR = (By.ID, "jivo_close_button")


class LoginPageLocators:
    """Локаторы для Страницы входа."""
    # Ищем поле email
    USERNAME_INPUT = (By.CSS_SELECTOR, ".form_input[name='email']")
    
    # Ищем поле password ТОЛЬКО внутри формы с классом fn_validate_login
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".form_input[name='password']")
    
    # Кнопка "Войти" внутри той же формы
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".button[name='login']")
    
    # Сообщение об ошибке
    ERROR_MESSAGE = (By.CLASS_NAME, "message_error")


class CookieBannerLocators:
    """Локаторы для баннера согласия с cookies"""
    # Кнопка "Принять"
    ACCEPT_BUTTON = (By.ID, "acceptCookies")
