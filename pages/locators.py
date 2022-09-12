from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_link')
