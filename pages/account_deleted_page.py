from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DeletedAccountPage(BasePage):
    ACCOUNT_DELETED_LOCATOR = (By.CSS_SELECTOR,"h2[data-qa='account-deleted']")
    CONTINUE_BTN_LOCATOR = (By.CSS_SELECTOR,"a[data-qa='continue-button']")

    def click_continue_btn(self):
        self.click(self.CONTINUE_BTN_LOCATOR)

    def is_account_deleted(self):
        return self.wait_for_element(self.ACCOUNT_DELETED_LOCATOR).text