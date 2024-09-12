from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    # def return_to_home_page(self):
    #     wd = self.wd
    #     # Go to home page ?
    #     wd.find_element_by_link_text("home page").click()
    #
    # def submit_new_user(self):
    #     wd = self.wd
    #     # submit new user
    #     wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
    #     self.return_to_home_page()
    #
    # def fill_new_user(self, user):
    #     wd = self.wd
    #     self.open_add_new_page()
    #     # fill new user
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(user.firstname)
    #     wd.find_element_by_name("middlename").click()
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys(user.middlename)
    #     wd.find_element_by_name("lastname").click()
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(user.lastname)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(user.address)
    #     wd.find_element_by_name("home").click()
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys(user.homephone)
    #     wd.find_element_by_name("mobile").click()
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(user.mobilephone)
    #     wd.find_element_by_name("work").click()
    #     wd.find_element_by_name("work").clear()
    #     wd.find_element_by_name("work").send_keys(user.workphone)
    #     self.submit_new_user()
    #
    # def open_add_new_page(self):
    #     wd = self.wd
    #     # Open add new page
    #     wd.find_element_by_link_text("add new").click()
