from page_objects.upload_page import UploadPage

class UploadTest(UploadPage):
    def test_visible_upload(self):
        # open page
        self.open_page_upload()
        # get file path
        file_path = "D:\Code\Python\seleniumPython\data\steak.jpg"
        # upload file
        self.choose_file(UploadPage.file_upload_visible, file_path)
        # click the upload button
        self.click(UploadPage.file_submit_visible)
        #assert file uploaded text
        self.assert_text("File Uploaded!", UploadPage.uploaded_text_visible)

    def test_hidden_upload(self):
        # open page
        self.open_page_cart()
        # get file path
        file_path = "D:\Code\Python\seleniumPython\data\steak.jpg"
        # add js code
        # remove_js_class = "document.querySelector('#upfile_1').classList.remove('file_input_hidden')"
        remove_hidden_class = f"document.querySelector({UploadPage.file_upload_hidden}).classList.remove({UploadPage.hidden_class})"
        self.add_js_code(remove_hidden_class)
        # upload file
        self.choose_file(UploadPage.file_upload_hidden, file_path)
        # click the upload button
        self.click(UploadPage.file_upload_btn)
        # assert file uploaded text
        self.assert_text("uploaded successfully", UploadPage.file_upload_text)