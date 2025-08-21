from seleniumbase import BaseCase

class ShopPage(BaseCase):
    search_bar = '#woocommerce-product-search-field-0'
    search_btn = 'button[value="Search"]'
    image = '.woocommerce-product-gallery__wrapper'

    def open_page(self):
        self.open("https://practice.sdetunicorns.com/shop/")