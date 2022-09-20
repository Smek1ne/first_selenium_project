from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_link')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form>button')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, '#messages .alertinner>strong')
    TOTAL_PRICE = (By.CSS_SELECTOR, '#messages .alertinner p strong')
    CART = (By.CSS_SELECTOR, '#add_to_basket_form > button')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_BLOCK = (By.CSS_SELECTOR, '.basket-mini')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_ITEMS_BLOCK = (By.CSS_SELECTOR, '#basket_formset')
