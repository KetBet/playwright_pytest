from playwright.sync_api import Page


class ContactUsPage():
    def __init__(self, page: Page):
        self.page = page
        self.contact_form_title = self.page.locator('.contact-form>h2.title')
        self.name_field = self.page.locator('input[data-qa="name"]')
        self.email_field = self.page.locator('input[data-qa="email"]')
        self.subject_field = self.page.locator('input[data-qa="subject"]')
        self.message_field = self.page.locator('#message')
        self.choose_file_btn = self.page.locator('input[name="upload_file"]')
        self.submit_btn = self.page.locator('input[data-qa="submit-button"]')
        self.alert_msg = self.page.locator('.status.alert.alert-success')
        self.home_btn = self.page.locator('//span[text()=" Home"]')

    def fill_contact_us_form(self, name, email, subject, message) -> None:
        self.name_field.fill(name)
        self.email_field.fill(email)
        self.subject_field.fill(subject)
        self.message_field.fill(message)

    def upload_file(self, file) -> None:
        self.choose_file_btn.set_input_files(file)

    def click_submit_btn(self) -> None:
        self.submit_btn.click()

    def click_ok(self) -> None:
        def handle_dialog(dialog):
            dialog.accept()

        self.page.on('dialog', handle_dialog)
        self.submit_btn.click()
        #self.page.on("dialog", lambda dialog: dialog.accept())

    def click_home_btn(self) -> None:
        self.home_btn.click()

