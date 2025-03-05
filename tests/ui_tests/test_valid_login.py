from pages.homepage import HomePage
from pages.signup_signin_page import SignupSigninPage
from pages.account_deleted_page import DeletedAccountPage

class TestValidLogin:
    EMAIL = "admin_majd@gmail.com"
    PASSWORD = "testautomatiom"
    NAME = "admin"

    def test_valid_login(self,setup):
        self.driver = setup
        homepage = HomePage(self.driver)
        homepage.open()
        assert homepage.is_logo_displayed(), "Homepage logo is not visible"
        homepage.go_to_signup_login_page()

        signuppage = SignupSigninPage(self.driver)
        signuppage.login(self.EMAIL, self.PASSWORD)

        assert homepage.is_username_visible() == self.NAME

        accountdeleted = DeletedAccountPage(self.driver)
        homepage.click_delete_account()
        assert accountdeleted.is_account_deleted() == "ACCOUNT DELETED!"
        accountdeleted.click_continue_btn()



