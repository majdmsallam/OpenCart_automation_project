from time import sleep

import pytest
from pages.homepage import HomePage

class TestHomePage:

    def test_homepage_title(self, setup):
        """Verifies the title of the homepage."""
        self.driver = setup
        homepage = HomePage(self.driver)
        homepage.open()
        assert homepage.get_title() == "Automation Exercise"

    def test_logo_visibility(self, setup):
        """Checks if the store logo is visible."""
        self.driver = setup
        homepage = HomePage(self.driver)
        self.driver.get("https://www.automationexercise.com/")
        assert homepage.is_logo_displayed()
