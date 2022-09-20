from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'No "login" in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form on page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'No register form on page'
        # assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
