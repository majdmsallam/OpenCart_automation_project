from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    ACCOUNT_CREATED_LOCATOR = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BTN_LOCATOR = (By.CSS_SELECTOR, "a[data-qa='continue-button']")


    def is_account_created(self):
        return self.wait_for_element(self.ACCOUNT_CREATED_LOCATOR).text

    def click_continue_btn(self):
        self.click(self.CONTINUE_BTN_LOCATOR)