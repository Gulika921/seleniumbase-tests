from seleniumbase import BaseCase

class HomePage(BaseCase):
    logo_icon = ".custom-logo-link"
    get_started_btn = "#get-started"
    heading_text = "h1"
    copyright_text = ".zak-footer-bar__1"
    menu_links = "#zak-primary-menu li[id*=menu-item]"
    username = '#username'
    password = '#password'
    btn = "button[value='Log in']"
    login_check = ".woocommerce-MyAccount-content"
    logout_btn = ".woocommerce-MyAccount-content a[href*='logout']"
    logout_check = ".u-column1"

    def open_page(self):
        self.open("https://practice.sdetunicorns.com/")

    def login(self):
        self.open("https://practice.sdetunicorns.com/my-account/")
        self.send_keys(self.username, "testuser")
        self.send_keys(self.password, "PracticeSite123!!")
        self.click(self.btn)
        self.assert_text("Log out", self.login_check)

    def logout(self):
        self.open("https://practice.sdetunicorns.com/my-account/")
        self.click(self.logout_btn)
        self.assert_text("Login", self.logout_check)