import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from data.data import Data
from utils.tools import take_screenshot

product_name = Data.product["name"]


class TestProductsPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = ProductsPage(self.page)
        self.product_details_page = ProductDetailsPage(self.page)
        assert self.page.title() == 'Automation Exercise'

        self.home_page.click_products_btn()
        assert self.page.url == 'https://automationexercise.com/products'

    def test_verify_all_products_and_product_detail_page(self, test_setup):
        """Test to verify all products and product detail page

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        assert self.products_page.all_products_list.is_visible()

        self.products_page.click_first_product_view_link()
        assert self.page.url == 'https://automationexercise.com/product_details/1'

        assert self.product_details_page.product_name.is_visible()
        assert self.product_details_page.product_category.is_visible()
        assert self.product_details_page.product_price.is_visible()
        assert self.product_details_page.product_availability.is_visible()
        assert self.product_details_page.product_condition.is_visible()
        assert self.product_details_page.product_brand.is_visible()

        take_screenshot(self.page, "Verify All Products and product detail page")

    def test_search_product(self, test_setup):
        """Test to verify the products search functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.products_page.search_by_name(product_name)
        assert self.products_page.search_results_title.is_visible()

        self.products_page.check_results_by_name(product_name)

        take_screenshot(self.page, "Search Product")