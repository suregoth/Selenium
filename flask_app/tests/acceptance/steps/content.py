from behave import *
from tests.acceptance.page_model.base_page import BasePage

# import sys
# sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/page_model")
# from base_page import BasePage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()

@step('The title tag gas content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content

@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()

@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.browser)
    tags = page.posts

    posts_with_title = [post for post in tags if post.text == title]

    assert len(posts_with_title) > 0