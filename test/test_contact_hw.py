# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="Dune", middlename="John", lastname="Smith", address="str. Beverly", homephone="+5-510-610", mobilephone="+1-(715)-43-269", workphone="3205846"))
    app.session.logout()


def test_add_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="", middlename="", lastname="", address="", homephone="", mobilephone="", workphone=""))
    app.session.logout()
