from page_objects.home_page import HomePage

class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        print("Running before each test")
        # log in
        self.login()
        # open home page
        self.open_page()

    def tearDown(self):
        print("Running after each test")
        #log out
        self.logout()

        super().tearDown()

    def test_home_page(self):

        # assert page title
        self.assert_title("Practice E-Commerce Site – SDET Unicorns")
        # assert logo
        self.assert_element(HomePage.logo_icon)

        # click on the get started button and assert the url
        self.click(HomePage.get_started_btn)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url ,"https://practice.sdetunicorns.com/#get-started")
        self.assert_true("get-started" in get_started_url)
        # self.assert_url("https://practice.sdetunicorns.com/#get-started")

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", HomePage.heading_text)

        # Exercise: scroll to bottom and assert the copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 SDET Unicorns", HomePage.copyright_text)

    def test_manu_links(self):
        expected_links = ["Home", "About", "Shop", "Blog", "Contact", "My account"]


        # find menu links elements
        menu_links_el = self.find_elements(HomePage.menu_links)
        # self.find_elements("//ul[@id='zak-primary-menu']/descendant::li")

        # loop through our menu links
        for idx, link_el in enumerate(menu_links_el):
            print(idx, link_el.text)
            self.assert_equal(expected_links[idx], link_el.text)