from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupSigninPage(BasePage):
    LOGIN_EMAIL_ADDRESS_LOCATOR = (By.CSS_SELECTOR,"input[data-qa='login-email']")
    LOGIN_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR,"button[data-qa='login-button']")

    SIGNUP_NAME_LOCATOR = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_ADDRESS_LOCATOR = (By.CSS_SELECTOR,"input[data-qa='signup-email']")
    SIGNUP_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def login(self,email, password):
        self.send_keys(self.LOGIN_EMAIL_ADDRESS_LOCATOR,email)
        self.send_keys(self.LOGIN_PASSWORD_LOCATOR, password)
        self.click(self.LOGIN_BUTTON_LOCATOR)

    def signup(self,name, email):
        self.send_keys(self.SIGNUP_NAME_LOCATOR, name)
        self.send_keys(self.SIGNUP_EMAIL_ADDRESS_LOCATOR, email)
        self.click(self.SIGNUP_BUTTON_LOCATOR)