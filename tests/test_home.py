import pytest

from pages.home_page import HomePage
from faker import Faker
from utils.tools import take_screenshot

fake = Faker()

email = fake.email()


class TestHomePage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        assert self.page.title() == 'Automation Exercise'

    def test_verify_subscription_in_home_page(self, test_setup):
        """Test to verify the subscription functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        assert self.home_page.subscription_title.inner_text() == 'SUBSCRIPTION'
        self.home_page.fill_subscription_form(email)

        assert self.home_page.success_alert_msg.is_visible()

        take_screenshot(self.page, "Verify Subscription in home page")
