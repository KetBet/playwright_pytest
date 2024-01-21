import pytest
import random

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.acc_created_page import AccCreatedPage
from pages.acc_deleted_page import AccDeletedPage
from data.data import Data
from faker import Faker
from utils.tools import take_screenshot

fake = Faker()

nameSignup = fake.name()
emailSignup = fake.email()
passwordSignup = fake.password()
genderSignup = random.randint(1, 2)
birth_day = Data.new_user["birth_day"]
birth_month = Data.new_user["birth_month"]
birth_year = Data.new_user["birth_year"]
first_name = fake.first_name()
last_name = fake.last_name()
company = fake.bs()
address1 = fake.address()
address2 = fake.secondary_address()
country = Data.new_user["country"]
state = fake.state()
city = fake.city()
zipcode = fake.zipcode()
phone = fake.basic_phone_number()

user_email = Data.user["email"]
user_password = Data.user["password"]
user_name = Data.user["name"]


class TestRegistrationPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.login_page = LoginPage(self.page)
        self.registration_page = RegistrationPage(self.page)
        self.acc_created_page = AccCreatedPage(self.page)
        self.acc_deleted_page = AccDeletedPage(self.page)
        assert self.page.title() == 'Automation Exercise'

    def test_register_user(self, test_setup):
        """Test to verify the user registration with valid credentials

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.click_signup_login_link()
        assert self.login_page.signup_form_title.is_visible()

        self.login_page.fill_signup_form(nameSignup, emailSignup)
        self.login_page.click_signup_btn()
        assert self.registration_page.form_title.first.is_visible()

        self.registration_page.fill_acc_info_form(genderSignup, passwordSignup, birth_day, birth_month, birth_year)
        self.registration_page.select_newsletter_checkbox()
        self.registration_page.select_offers_checkbox()
        self.registration_page.fill_address_info_form(first_name, last_name, company, address1, address2, country, state, city, zipcode, phone)
        self.registration_page.click_create_acc_btn()
        assert self.acc_created_page.acc_created_title.is_visible()

        self.acc_created_page.click_continue_btn()
        assert self.home_page.logged_in_as_username.is_visible()

        assert nameSignup in self.home_page.logged_in_as_username.inner_text()

        self.home_page.click_delete_acc_btn()
        assert self.acc_deleted_page.acc_deleted_title.is_visible()

        self.acc_deleted_page.click_continue_btn()

        take_screenshot(self.page, "Register User")

    def test_register_user_with_existing_email(self, test_setup):
        """Test to verify new user registration with existing email

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.click_signup_login_link()
        assert self.login_page.login_form_title.is_visible()

        self.login_page.fill_signup_form(user_name, user_email)
        self.login_page.click_signup_btn()
        assert self.login_page.signup_form_error_msg.is_visible()

        take_screenshot(self.page, "Register User with existing email")
