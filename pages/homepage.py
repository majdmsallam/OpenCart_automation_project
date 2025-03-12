from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    PAGE_TITLE = (By.TAG_NAME,"title")
    LOGIN_SIGNUP_BAR = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    url = "https://www.automationexercise.com/"
    USERNAME_LOCATOR = (By.XPATH,"//b")
    DELETE_ACCOUNT_LOCATOR = (By.XPATH,"//a[contains(text(), 'Delete Account')]")
    CONTACT_US_LOCATOR = (By.XPATH,"//a[contains(text(), 'Contact us')]")
    PRODUCTS_LOCATOR = (By.XPATH,"//a[contains(text(), 'Products')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def is_logo_displayed(self):
        return self.wait_for_element(self.LOGO).is_displayed()

    def is_username_visible(self):
        return self.wait_for_element(self.USERNAME_LOCATOR).text

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_LOCATOR)

    def go_to_signup_login_page(self):
        self.click(self.LOGIN_SIGNUP_BAR)

    def go_to_contactus_page(self):
        self.click(self.CONTACT_US_LOCATOR)

    def go_to_products_page(self):
        self.click(self.PRODUCTS_LOCATOR)