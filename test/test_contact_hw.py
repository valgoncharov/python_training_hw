# -*- coding: utf-8 -*-
import pytest
from user import User
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_user(app):
    app.login(username="admin", password="secret")
    app.fill_new_user(User(firstname="iewrfnse", middlename="fsf", lastname="Poigl", address="str. Uhhfjfd", homephone="+5-585-6894", mobilephone="(99)-43-656", workphone="32425346"))
    app.logout()


def test_add_empty_user(app):
    app.login(username="admin", password="secret")
    app.fill_new_user(User(firstname="", middlename="", lastname="", address="", homephone="", mobilephone="", workphone=""))
    app.logout()
