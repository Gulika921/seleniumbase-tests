from seleniumbase import BaseCase

class UploadPage(BaseCase):
    file_upload_visible = "#file-upload"
    file_submit_visible = "#file-submit"
    uploaded_text_visible = ".example"
    file_upload_hidden = "#upfile_1"
    hidden_class = "file_input_hidden"
    file_upload_btn = "#upload_1"
    file_upload_text = "#wfu_messageblock_header_1_1"

    def open_page_upload(self):
        self.open("https://the-internet.herokuapp.com/upload")

    def open_page_cart(self):
        self.open("https://practice.sdetunicorns.com/cart/")
