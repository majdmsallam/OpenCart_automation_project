from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUSPage(BasePage):
    CONTACT_PAGE_LOCATOR = (By.ID,"contact-page")
    NAME_LOCATOR = (By.CSS_SELECTOR,"input[data-qa='name']")
    EMAIL_LOCATOR = (By.CSS_SELECTOR,"input[data-qa='email']")
    SUBJECT_LOCATOR = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE_LOCATOR = (By.CSS_SELECTOR,"textarea[data-qa='message']")
    UPLOAD_FILE_LOCATOR = (By.CSS_SELECTOR, "input[name='upload_file']")
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    SUCCESS_ALERT_LOCATOR = (By.XPATH, "//div[@class='status alert alert-success']")
    HOME_BUTTON_LOCATOR = (By.XPATH, "//div[@id='form-section']//a")

    def is_page_displayed(self):
        return self.wait_for_element(self.CONTACT_PAGE_LOCATOR).is_displayed()

    def fill_name(self, name):
        self.send_keys(self.NAME_LOCATOR, name)

    def fill_email(self, email):
        self.send_keys(self.EMAIL_LOCATOR, email)

    def fill_subject(self, subject):
        self.send_keys(self.SUBJECT_LOCATOR, subject)

    def fill_message(self, msg):
        self.send_keys(self.MESSAGE_LOCATOR, msg)

    def upload_file(self, file_path):
        self.send_keys(self.UPLOAD_FILE_LOCATOR, file_path)

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON_LOCATOR)

    def is_success_alert_displayed(self):
        return self.wait_for_element(self.SUCCESS_ALERT_LOCATOR).is_displayed()

    def click_home_button(self):
        self.click(self.HOME_BUTTON_LOCATOR)
