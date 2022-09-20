from .base_page import BasePage
from .locators import ProductPageLocators as L
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def should_be_cart_link(self):
        assert self.is_element_present(*L.CART)

    def cart_click(self):
        self.browser.find_element(*L.CART).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_name_in_success_message_is_correct(self):
        product_name = self.browser.find_element(*L.PRODUCT_NAME)
        success_messages = self.browser.find_element(*L.SUCCESS_MESSAGES)

        assert product_name.text == success_messages.text, 'Invalid product name in success message'

    def cart_total_price_equals_product_price(self):
        product_price = self.browser.find_element(*L.PRODUCT_PRICE)
        total_price = self.browser.find_element(*L.TOTAL_PRICE)

        assert total_price.text == product_price.text, 'Total price is not equal to the product price'

    def should_not_be_success_message(self):
        assert self.element_is_not_presented(*L.SUCCESS_MESSAGES), \
            "Success message is presented, but shouldn't be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*L.SUCCESS_MESSAGES), \
            "Success message did not disappear"
