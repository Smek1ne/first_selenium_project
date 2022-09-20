from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            'There is no message that basket is empty'

    def should_not_be_items_in_the_basket(self):
        assert self.element_is_not_presented(*BasketPageLocators.BASKET_ITEMS_BLOCK), \
            'Items are in the basket but should not be'
