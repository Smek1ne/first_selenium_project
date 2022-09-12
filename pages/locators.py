from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGES = (By.CSS_SELECTOR, '#messages .alertinner>strong')
    TOTAL_PRICE = (By.CSS_SELECTOR, '#messages .alertinner p strong')
    CART = (By.CSS_SELECTOR, '#add_to_basket_form > button')