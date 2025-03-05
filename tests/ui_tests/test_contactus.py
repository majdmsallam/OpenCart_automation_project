from time import sleep

from pages.homepage import HomePage
from pages.contactus_page import ContactUSPage

class TestContactUs:
    NAME = "admin"
    EMAIL = "admin_majd@gmail.com"
    SUBJECT = "test automation"
    MESSAGE = "My skills in selenium are getting better!"
    PATH_TO_FILE = "C:\\test\\sample_sales_data.csv"

    def test_contactus(self, setup):
        self.driver = setup
        homepage = HomePage(self.driver)
        homepage.open()

        assert homepage.is_logo_displayed()

        homepage.go_to_contactus_page()
        contactuspage = ContactUSPage(self.driver)
        assert contactuspage.is_page_displayed()

        contactuspage.fill_name(self.NAME)
        contactuspage.fill_email(self.EMAIL)
        contactuspage.fill_subject(self.SUBJECT)
        contactuspage.fill_message(self.MESSAGE)
        contactuspage.upload_file(self.PATH_TO_FILE)
        contactuspage.click_submit_button()

        alert = self.driver.switch_to.alert
        alert.accept()

        assert contactuspage.is_success_alert_displayed()

        contactuspage.click_home_button()
        assert homepage.is_logo_displayed()

