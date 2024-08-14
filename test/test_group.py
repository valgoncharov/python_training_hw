# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name="fqwefaef", header="faewf", footer="faf"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
