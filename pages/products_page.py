from playwright.sync_api import Page
from playwright.sync_api import expect


class ProductsPage():
    def __init__(self, page: Page):
        self.page = page
        self.all_products_list = self.page.locator('.features_items')
        self.first_product_view_link = self.page.locator('.nav-justified')
        self.search_field = self.page.locator('#search_product')
        self.search_btn = self.page.locator('#submit_search')
        self.search_results_title = self.page.locator('.features_items>h2')
        self.searched_products_names = self.page.locator('.productinfo>p')

    def click_first_product_view_link(self) -> None:
        self.first_product_view_link.first.click()

    def search_by_name(self, product_name) -> None:
        self.search_field.fill(product_name)
        self.search_btn.click()

    def check_results_by_name(self, product_name) -> None:
        results = self.searched_products_names.all_inner_texts()
        assert all(product_name in result for result in results)