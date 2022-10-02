import unittest, platform
from selenium import webdriver
import page

if platform.system() == "Linux":
    PATH = '/opt/selenium/chromedriver'
elif platform.system() == "Windows":
    PATH = 'C:\sel\chromedriver.exe'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")

    def test_example(self):
        print("test")
        assert True

    def not_a_test(self):
        print("not a test")
        
    def tearDown(self):
        self.driver.close()