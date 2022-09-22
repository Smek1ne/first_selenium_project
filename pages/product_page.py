from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.CART)

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.CART).click()

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
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_messages = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGES)

        assert product_name.text == success_messages.text, 'Invalid product name in success message'

    def cart_total_price_equals_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)

        assert total_price.text == product_price.text, 'Total price is not equal to the product price'

    def should_not_be_success_message(self):
        assert self.element_is_not_presented(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is presented, but shouldn't be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message did not disappear"
