from playwright.sync_api import Page

class AccCreatedPage():
    def __init__(self, page: Page):
        self.page = page
        self.acc_created_title = self.page.locator('h2[data-qa="account-created"]')
        self.continue_btn = self.page.locator('[data-qa="continue-button"]')

    def click_continue_btn(self) -> None:
        self.continue_btn.click()