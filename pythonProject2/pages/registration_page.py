from playwright.sync_api import Page

class RegistrationPage():
    def __init__(self, page: Page):
        self.page = page
        self.form_title = self.page.locator('h2.title.text-center > b')
        self.gender1_radio_btn = self.page.locator('#id_gender1')
        self.gender2_radio_btn = self.page.locator('#id_gender2')
        self.password_field = self.page.locator('#password')
        self.day_dropdown = self.page.locator('#days')
        self.month_dropdown = self.page.locator('#months')
        self.year_dropdown = self.page.locator('#years')
        self.news_checkbox = self.page.locator('#newsletter')
        self.offers_checkbox = self.page.locator('#optin')
        self.first_name_field = self.page.locator('#first_name')
        self.last_name_field = self.page.locator('#last_name')
        self.company_field = self.page.locator('#company')
        self.address1_field = self.page.locator('#address1')
        self.address2_field = self.page.locator('#address2')
        self.country_dropdown = self.page.locator('#country')
        self.state_field = self.page.locator('#state')
        self.city_field = self.page.locator('#city')
        self.zipcode_field = self.page.locator('#zipcode')
        self.mobile_number_field = self.page.locator('#mobile_number')
        self.create_acc_btn = self.page.locator('button[data-qa="create-account"]')

    def fill_acc_info_form(self, random_gender, random_password, day, month, year) -> None:
        if random_gender == 1:
            self.gender1_radio_btn.check()
        else:
            self.gender2_radio_btn.check()
        self.password_field.fill(random_password)
        self.day_dropdown.select_option(day)
        self.month_dropdown.select_option(month)
        self.year_dropdown.select_option(year)

    def fill_address_info_form(self, firstname, lastname, company, address, address2, country, state, city, zipcode,
                               mobile) -> None:
        self.first_name_field.fill(firstname)
        self.last_name_field.fill(lastname)
        self.company_field.fill(company)
        self.address1_field.fill(address)
        self.address2_field.fill(address2)
        self.country_dropdown.select_option(country)
        self.state_field.fill(state)
        self.city_field.fill(city)
        self.zipcode_field.fill(zipcode)
        self.mobile_number_field.fill(mobile)

    def select_newsletter_checkbox(self) -> None:
        self.news_checkbox.check()

    def select_offers_checkbox(self) -> None:
        self.offers_checkbox.check()

    def click_create_acc_btn(self) -> None:
        self.create_acc_btn.click()