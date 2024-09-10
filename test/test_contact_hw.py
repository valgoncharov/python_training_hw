# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_new_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.fill_new_user(wd, firstname="iewrfnse", middlename="fsf", lastname="Poigl", address="str. Uhhfjfd", homephone="+5-585-6894", mobilephone="(99)-43-656", workphone="32425346")
        self.submit_new_user(wd)
        self.go_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.fill_new_user(wd, firstname="", middlename="", lastname="", address="", homephone="", mobilephone="", workphone="")
        self.submit_new_user(wd)
        self.go_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # loguot
        wd.find_element_by_link_text("Logout").click()

    def go_to_home_page(self, wd):
        # Go to home page ?
        wd.find_element_by_link_text("home page").click()

    def submit_new_user(self, wd):
        # submit new user
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def fill_new_user(self, wd, firstname, middlename, lastname, address, homephone, mobilephone, workphone):
        # fill new user
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(workphone)

    def open_add_new_page(self, wd):
        # Open add new page
        wd.find_element_by_link_text("add new").click()
        # wd.get("http://localhost/addressbook/edit.php")

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/")

    # wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
