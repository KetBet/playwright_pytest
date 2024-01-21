import pytest
import os

from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from faker import Faker
from utils.tools import take_screenshot

scriptPath = os.path.abspath(__file__)
filePath = os.path.join(os.path.dirname(scriptPath), '..', 'data', 'croissant.jpg')

fake = Faker()
random_name = fake.name()
random_email = fake.email()
random_subject = fake.word()
random_message = fake.text()


class TestContactUsPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.contact_us_page = ContactUsPage(self.page)
        assert self.page.title() == 'Automation Exercise'

    def test_contact_us_form(self, test_setup):
        """Test to verify the contact us form

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.home_page.click_contact_us_btn()
        assert self.contact_us_page.contact_form_title.is_visible()

        self.contact_us_page.fill_contact_us_form(random_name, random_email, random_subject, random_message)
        self.contact_us_page.upload_file(filePath)
        self.contact_us_page.click_submit_btn()
        self.contact_us_page.click_ok()
        #assert self.contact_us_page.alert_msg.is_visible()
        #assert self.contact_us_page.alert_msg.inner_text() == 'Success! Your details have been submitted successfully.'

        self.home_page.click_home_btn()
        assert self.page.url == 'https://automationexercise.com/'

        take_screenshot(self.page, "Contact Us Form")
