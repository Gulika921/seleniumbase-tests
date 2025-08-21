import time

from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys

class CartTest(CartPage):

    def setUp(self):
        super().setUp()
        self.open("https://practice.sdetunicorns.com/shop/")

    def test_add_to_cart(self):
        # add item to the cart
        self.click(self.headphone_add_to_cart)

        # assert product is added to the cart
        self.assert_text("1", self.cart_count_text)

        # open cart page
        self.open_page()

        # get current subtotal
        text = self.get_text(self.product_subtotal)
        print(text) #200$

        # change cart quantity
        self.type(self.cart_quantity, "2") #"2\n
        # self.set_value(self.cart_quantity, "2")
        # self.send_keys(self.cart_quantity, Keys.RETURN)
        self.click(self.update_cart_btn)

        # wait a few seconds
        # time.sleep(3)

        # wait for loading to be completed
        # self.wait_for_element_visible(".blockOverlay")
        # self.wait_for_element_not_visible(".blockOverlay")

        # assert subtotal to be different from the original subtotal
        self.wait_for_text("$400.00", self.product_subtotal)
        updated_text = self.get_text(self.product_subtotal)
        print(updated_text)
        self.assert_not_equal(text, updated_text)