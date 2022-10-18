import unittest, platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import page

unittest.main(warnings='ignore')

options = Options()

if platform.system() == "Linux":
    PATH = Service('/opt/selenium/chromedriver')
elif platform.system() == "Windows":
    PATH = Service('C:\sel\chromedriver.exe')

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH, options=options)
        self.driver.get("http://www.python.org")

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_maching()

    def test_example(self):
        print("test")
        assert True

    def not_a_test(self):
        print("not a test")
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()