from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.locators.base_page import BasePageLocators

# import sys
# sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/locators")
# from base_page import BasePageLocators
# sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/locators")
# from home_page import HomePageLocators

class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)