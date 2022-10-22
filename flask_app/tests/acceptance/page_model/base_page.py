# from tests.acceptance.locators.base_page import BasePageLocators

import sys
sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/locators")
from base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000/'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)