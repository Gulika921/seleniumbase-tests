from seleniumbase import BaseCase

class CartPage(BaseCase):

    headphone_add_to_cart = 'a[data-product_id="361"]'
    cart_count_text = "span.count"
    product_subtotal = "td.product-subtotal"
    cart_quantity = 'input[aria-label="Product quantity"]'
    update_cart_btn = 'button[name="update_cart"]'

    def open_page(self):
        self.open("https://practice.sdetunicorns.com/cart/")