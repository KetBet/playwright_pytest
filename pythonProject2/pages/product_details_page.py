from playwright.sync_api import Page

class ProductDetailsPage():
    def __init__(self, page: Page):
        self.page = page
        self.product_name = self.page.locator('.product-information>h2')
        self.product_category = self.page.locator('//p[starts-with(text(), "Category:")]')
        self.product_price = self.page.locator('.product-information>span>span')
        self.product_availability = self.page.locator('//p[starts-with(b/text(), "Availability:")]')
        self.product_condition = self.page.locator('//p[starts-with(b/text(), "Condition:")]')
        self.product_brand = self.page.locator('//p[starts-with(b/text(), "Brand:")]')