from behave import *
from tests.acceptance.page_model.home_page import BasePage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()

@step('The title tag gas content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content