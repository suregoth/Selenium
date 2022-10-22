from tests.acceptance.page_model.base_page import BasePage

# import sys
# sys.path.append("/home/bambisien/git/Selenium/flask_app/templates/tests/acceptance/page_model")
# from base_page import BasePage

class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)