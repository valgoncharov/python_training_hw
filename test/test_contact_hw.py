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
    app.fill_new_user(Contact(firstname="Finse", middlename="Brad", lastname="Loki", address="str. Xikol", homephone="+5-585-6894", mobilephone="+1-(753)-43-656", workphone="32425346"))
    app.session.logout()


def test_add_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.fill_new_user(Contact(firstname="", middlename="", lastname="", address="", homephone="", mobilephone="", workphone=""))
    app.session.logout()
