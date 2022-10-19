import platform
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

use_step_matcher('re')

if platform.system() == "Linux":
    PATH = Service('/opt/selenium/chromedriver')
elif platform.system() == "Windows":
    PATH = Service('C:\sel\chromedriver.exe')

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('/opt/selenium/chromedriver')
    context.driver.get('http://127.0.0.1:5000')

@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('/opt/selenium/chromedriver')
    context.driver.get('http://127.0.0.1:5000/blog')

@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url