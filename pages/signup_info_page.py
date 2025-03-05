from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class SignupInfoPage(BasePage):
    MR_LOCATOR = (By.ID, "id_gender1")
    MRS_LOCATOR = (By.ID, "id_gender2")
    PASSWORD_LOCATOR = (By.ID, "password")
    DAY_LOCATOR = (By.ID, "days")
    MONTH_LOCATOR = (By.ID, "months")
    YEAR_LOCATOR = (By.ID, "years")
    FIRST_NAME_LOCATOR = (By.ID, "first_name")
    LAST_NAME_LOCATOR = (By.ID, "last_name")
    COMPANY_LOCATOR = (By.ID, "company")
    ADDRESS_LOCATOR = (By.ID, "address1")
    STATE_LOCATOR = (By.ID, "state")
    CITY_LOCATOR = (By.ID, "city")
    ZIPCODE_LOCATOR = (By.ID, "zipcode")
    MOBILE_NUMBER_LOCATOR = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[data-qa='create-account']")


    def click_title(self):
        radio_button = self.wait_for_element(self.MR_LOCATOR)
        if not radio_button.is_selected():
            radio_button.click()

    def fill_password(self, password):
        self.send_keys(self.PASSWORD_LOCATOR, password)

    def fill_birth_date(self):
        dropdown = self.wait_for_element(self.DAY_LOCATOR)
        select = Select(dropdown)
        select.select_by_visible_text("13")

        dropdown = self.wait_for_element(self.MONTH_LOCATOR)
        select = Select(dropdown)
        select.select_by_visible_text("August")

        dropdown = self.wait_for_element(self.YEAR_LOCATOR)
        select = Select(dropdown)
        select.select_by_visible_text("2006")

    def fill_first_name(self, name):
        self.send_keys(self.FIRST_NAME_LOCATOR, name)

    def fill_last_name(self, lastname):
        self.send_keys(self.LAST_NAME_LOCATOR, lastname)

    def fill_company(self, company):
        self.send_keys(self.COMPANY_LOCATOR, company)

    def fill_address(self, address):
        self.send_keys(self.ADDRESS_LOCATOR, address)

    def fill_state(self, state):
        self.send_keys(self.STATE_LOCATOR, state)

    def fill_city(self, city):
        self.send_keys(self.CITY_LOCATOR, city)

    def fill_zipcode(self, zipcode):
        self.send_keys(self.ZIPCODE_LOCATOR, zipcode)

    def fill_mobile_number(self, mobile_number):
        self.send_keys(self.MOBILE_NUMBER_LOCATOR, mobile_number)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON_LOCATOR)


