import platform
from behave import *
from selenium import webdriver
from tests.acceptance.locators.home_page import HomePage
from tests.acceptance.locators.blog_page import BlogPage

use_step_matcher('re')

if platform.system() == "Linux":
    PATH = '/opt/selenium/chromedriver'
elif platform.system() == "Windows":
    PATH = 'C:\sel\chromedriver.exe'

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(PATH)
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(PATH)
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url