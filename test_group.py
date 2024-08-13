# -*- coding: utf-8 -*-
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from application import Application
import unittest


@pytest.fixture
def app():
    fixture = Application()
    return fixture


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_group(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_group_page()
        self.app.create_group(Group(name="fqwefaef", header="faewf", footer="faf"))
        self.app.return_to_groups_page()
        self.app.logout()

    def test_add_empty_group(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_group_page()
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.return_to_groups_page()
        self.app.logout()



    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
