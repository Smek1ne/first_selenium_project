from pages.product_page import ProductPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_add_product_to_the_cart(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_cart_link()
    page.cart_click()
    page.solve_quiz_and_get_code()
    page.product_name_in_success_message_is_correct()
    page.cart_total_price_equals_product_price()
