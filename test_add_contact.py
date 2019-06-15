# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Liliia", middlename="Uralovna", lastname="Kuzyeva", nickname="chebi", title="Tester", company="Bank", address="Ekaterinburg, Surikova 60, apt 12", mobile="+79505471137", email="gilmirahman@gmail.com", address2="Ekaterinburg, Selkorovskaya, 2 apt 56"))
    app.logout()