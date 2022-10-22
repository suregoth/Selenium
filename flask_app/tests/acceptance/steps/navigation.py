import platform
from behave import *
from selenium import webdriver
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.pages.new_post_page import NewPostPage

# import sys
# sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/page_model")
# from blog_page import BlogPage
# sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/page_model")
# from home_page import HomePage

use_step_matcher('re')

if platform.system() == "Linux":
    PATH = '/opt/selenium/chromedriver'
elif platform.system() == "Windows":
    PATH = 'C:\sel\chromedriver.exe'

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('/opt/selenium/chromedriver')
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('/opt/selenium/chromedriver')
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = NewPostPage(context.browser)
    context.browser.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url