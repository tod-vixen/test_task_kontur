from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для Главной страницы."""

    # Ищем ссылку, где в тексте есть "Вход" или в адресе (href) есть "login"/"auth"
    LOGIN_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Вход') or contains(@href, 'login') or contains(@href, 'auth')]",
    )
    # Ищем ссылку для выхода из системы
    LOGOUT_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Выход') or contains(@href, 'logout')]",
    )
    # Базовый признак загрузки страницы (тег <body>)
    MAIN_PAGE_INDICATOR = (By.TAG_NAME, "body")


class LoginPageLocators:
    """Локаторы для Страницы входа."""

    # Поле логина: проверяем самые частые названия атрибутов на сайтах (включая 1С-Битрикс и OpenCart)
    USERNAME_INPUT = (
        By.XPATH,
        "//input[@name='USER_LOGIN' or @name='login' or @name='email' or @id='username' or @id='login']",
    )
    # Поле пароля
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@name='USER_PASSWORD' or @name='password' or @id='password']",
    )
    # Кнопка отправки формы
    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@type='submit'] or //input[@type='submit' or contains(@value, 'Войти')]",
    )
    # Сообщение об ошибке: ищем текст, содержащий слова, указывающие на ошибку
    ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'неверн') or contains(text(), 'ошибк') or contains(text(), 'неправиль') or contains(text(), 'Invalid') or contains(text(), 'Error')]",
    )


class CookieBannerLocators:
    """Локаторы для баннера согласия с cookies."""

    # Ищем кнопку, в тексте которой есть слова: Принять, Согласен, OK, Accept (игнорируя регистр)
    ACCEPT_BUTTON = (
        By.XPATH,
        "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'принять') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'согласен') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'ok') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
    )

    # Запасной вариант: если кнопка не находится, попробуем найти сам контейнер баннера, чтобы скрыть его
    BANNER_CONTAINER = (
        By.XPATH,
        "//*[contains(@class, 'cookie') or contains(@id, 'cookie') or contains(@class, 'gdpr')]",
    )
