from tests.acceptance.page_model.base_page import BasePage

# import sys
# sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/page_model")
# from base_page import BasePage

class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self):
        return self.driver.find_element(*NewPostPageLocators.NEW_POST_FORM).find_element()

    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
