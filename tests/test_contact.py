from page_objects.contact_page import ContactPage

class ContactTest(ContactPage):
    def test_contact_page(self):
        # open page
        self.open_page()

         # scroll to the form and take screenshot
        self.highlight("#evf-form-277")
        self.save_screenshot("empty_contact_form", "../custom_screenshots")

        # fill in all the fields
        self.filling_in()

        # take screenshot when the form is filled
        self.highlight("#evf-form-277")
        self.save_screenshot("filled_contact_form", "../custom_screenshots")

        # click the submit button
        self.click(ContactPage.submit_button)
        #verify submit message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", ContactPage.submit_message)
