from playwright.sync_api import Page


class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.logo = self.page.locator('div.logo.pull-left')
        self.signup_login_link = self.page.locator('a[href="/login"]')
        self.logged_in_as_username = self.page.locator('li>a>b')
        self.delete_account_btn = self.page.locator('a[href="/delete_account"]')
        self.logout_btn = self.page.locator('a[href="/logout"]')
        self.contact_us_btn = self.page.locator('a[href="/contact_us"]')
        self.home_btn = self.page.locator('ul>li>a[href="/"]')
        self.test_cases_btn = self.page.locator('ul>li>a[href="/test_cases"]')
        self.products_btn = self.page.locator('ul>li>a[href="/products"]')
        self.subscription_title = self.page.locator('.single-widget>h2')
        self.subscription_field = self.page.locator('#susbscribe_email')
        self.subscription_btn = self.page.locator('#subscribe')
        self.success_alert_msg = self.page.locator('#success-subscribe>.alert-success')

    def click_signup_login_link(self) -> None:
        self.signup_login_link.click()

    def click_delete_acc_btn(self) -> None:
        self.delete_account_btn.click()

    def click_logout_btn(self) -> None:
        self.logout_btn.click()

    def click_contact_us_btn(self) -> None:
        self.contact_us_btn.click()

    def click_home_btn(self) -> None:
        self.home_btn.click()

    def click_test_cases_btn(self) -> None:
        self.test_cases_btn.click()

    def click_products_btn(self) -> None:
        self.products_btn.click()

    def fill_subscription_form(self, email) -> None:
        self.subscription_field.fill(email)
        self.subscription_btn.click()