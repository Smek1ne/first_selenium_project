from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_presented(By.CSS_SELECTOR, "#login_link"), 'Login link is not presented'
