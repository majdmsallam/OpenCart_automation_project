from pages.homepage import HomePage
from pages.signup_signin_page import SignupSigninPage

class TestValidLogin:
    EMAIL = "invalid@gmail.com"
    PASSWORD = "testautomatiom"


    def test_invalid_login(self,setup):
        self.driver = setup
        homepage = HomePage(self.driver)
        homepage.open()
        assert homepage.is_logo_displayed(), "Homepage logo is not visible"
        homepage.go_to_signup_login_page()

        signuppage = SignupSigninPage(self.driver)
        signuppage.login(self.EMAIL, self.PASSWORD)

        assert signuppage.is_incorrect_email_password(), "Error message for invalid login is not displayed"
