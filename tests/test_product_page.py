from pages.product_page import ProductPage
import pytest

# url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_add_product_to_the_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.cart_click()
    page.solve_quiz_and_get_code()
    page.product_name_in_success_message_is_correct()
    page.cart_total_price_equals_product_price()
