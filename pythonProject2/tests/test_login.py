import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.acc_created_page import AccCreatedPage
from pages.acc_deleted_page import AccDeletedPage
from data.data import Data
from faker import Faker
from utils.tools import take_screenshot
fake = Faker()

user_email = Data.user["email"]
user_password = Data.user["password"]
user_name = Data.user["name"]

email_invalid = fake.email()
password_invalid = fake.password()


class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.login_page = LoginPage(self.page)
        self.acc_created_page = AccCreatedPage(self.page)
        self.acc_deleted_page = AccDeletedPage(self.page)
        assert self.page.title() == 'Automation Exercise'

    def test_login_user_with_correct_email_and_password(self, test_setup):
        """Test to verify login with valid credentials

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.click_signup_login_link()
        assert self.login_page.login_form_title.is_visible()

        self.login_page.fill_login_form(user_email, user_password)
        self.login_page.click_login_btn()
        assert self.home_page.logged_in_as_username.is_visible()
        assert user_name in self.home_page.logged_in_as_username.inner_text()

        self.home_page.click_delete_acc_btn()
        assert self.acc_deleted_page.acc_deleted_title.is_visible()

        take_screenshot(self.page, "Login User with correct email and password")

    def test_login_user_with_incorrect_email_and_password(self, test_setup):
        """Test to verify login with invalid credentials

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.click_signup_login_link()
        assert self.login_page.login_form_title.is_visible()

        self.login_page.fill_login_form(email_invalid, password_invalid)
        self.login_page.click_login_btn()
        assert self.login_page.login_form_error_msg.is_visible()

        take_screenshot(self.page, "Login User with incorrect email and password")

    def test_logout_user(self, test_setup):
        """Test to verify the logout

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.click_signup_login_link()
        assert self.login_page.login_form_title.is_visible()

        self.login_page.fill_login_form(user_email, user_password)
        self.login_page.click_login_btn()
        assert self.home_page.logged_in_as_username.is_visible()
        assert user_name in self.home_page.logged_in_as_username.inner_text()

        self.home_page.click_logout_btn()
        assert self.page.url == 'https://automationexercise.com/login'

        take_screenshot(self.page, "Logout User")