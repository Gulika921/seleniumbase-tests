from seleniumbase import BaseCase

class ContactPage(BaseCase):
    contact_name = ".contact-name input"
    contact_email = ".contact-email input"
    contact_phone = ".contact-phone input"
    contact_message = ".contact-message textarea"
    submit_button = "#evf-submit-277"
    submit_message = ".everest-forms-notice"

    def open_page(self):
        self.open("https://practice.sdetunicorns.com/contact/")

    def filling_in(self):
        self.send_keys(self.contact_name, "fhfghr")
        self.send_keys(self.contact_email, "hffddfj@gmail.com")
        self.send_keys(self.contact_phone, "33434")
        self.send_keys(self.contact_message, "hfgbfuyfrbufurf")