from time import sleep

from pages.homepage import HomePage
from pages.signup_signin_page import SignupSigninPage
from pages.signup_info_page import SignupInfoPage
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import DeletedAccountPage

class TestSignUp:
    EMAIL = "majdmsallam1998@gmail.com"
    NAME = "Majd Msallam"


    def test_signup(self, setup):
        self.driver = setup
        homepage = HomePage(self.driver)
        homepage.open()
        assert homepage.is_logo_displayed(), "Homepage logo is not visible"

        homepage.go_to_signup_login_page()
        signuppage = SignupSigninPage(self.driver)
        signuppage.signup(self.NAME, self.EMAIL)
        signupinfopage = SignupInfoPage(self.driver)
        signupinfopage.click_title()
        signupinfopage.fill_password("testautomatiion")
        signupinfopage.fill_birth_date()
        signupinfopage.fill_first_name("Majd")
        signupinfopage.fill_last_name("Msallam")
        signupinfopage.fill_company("Y.M Pirzul")
        signupinfopage.fill_address("Nazareth")
        signupinfopage.fill_state("Nazareth")
        signupinfopage.fill_city("Nazareth")
        signupinfopage.fill_zipcode("16000")
        signupinfopage.fill_mobile_number("05231549848")
        signupinfopage.click_create_account()
        accountcreated = AccountCreatedPage(self.driver)
        assert accountcreated.is_account_created() == "ACCOUNT CREATED!"
        accountcreated.click_continue_btn()

        assert homepage.is_username_visible() == self.NAME

        accountdeleted = DeletedAccountPage(self.driver)
        homepage.click_delete_account()
        assert accountdeleted.is_account_deleted() == "ACCOUNT DELETED!"
        accountdeleted.click_continue_btn()




