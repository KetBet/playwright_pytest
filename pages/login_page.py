from playwright.sync_api import Page

class LoginPage():
    def __init__(self, page: Page):
        self.page = page
        self.signup_form_title = self.page.locator('.signup-form>h2')
        self.signup_name_field = self.page.locator('input[data-qa="signup-name"]')
        self.signup_email_field = self.page.locator('input[data-qa="signup-email"]')
        self.signup_button = self.page.locator('button[data-qa="signup-button"]')
        self.login_form_title = self.page.locator('.login-form>h2')
        self.login_email_field = self.page.locator('input[data-qa="login-email"]')
        self.login_password_field = self.page.locator('input[data-qa="login-password"]')
        self.login_button = self.page.locator('button[data-qa="login-button"]')
        self.login_form_error_msg = self.page.locator('form[action="/login"]>p')
        self.signup_form_error_msg = self.page.locator('form[action="/signup"]>p')

    def click_signup_btn(self) -> None:
        self.signup_button.click()

    def fill_signup_form(self, random_name, random_email) -> None:
        self.signup_name_field.fill(random_name)
        self.signup_email_field.fill(random_email)

    def fill_login_form(self, email, password) -> None:
        self.login_email_field.fill(email)
        self.login_password_field.fill(password)

    def click_login_btn(self) -> None:
        self.login_button.click()

