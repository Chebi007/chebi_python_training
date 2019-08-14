
from model.contact import Contact

def test_modify_firstname(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(firstname="Liliia modified"))
    app.session.logout()

def test_modify_middlename(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(middlename="Uralovna modified"))
    app.session.logout()

def test_modify_lastname(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(lastname="Kuzyeva edited"))
    app.session.logout()

def test_modify_nickname(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(nickname="chebi modified"))
    app.session.logout()

def test_modify_title(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(title="Tester modified"))
    app.session.logout()

def test_modify_company(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(company="Bank modified"))
    app.session.logout()

def test_modify_address(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(address="Ekaterinburg, Surikova 60, apt 12"))
    app.session.logout()

def test_modify_mobile(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(mobile="+79505471137"))
    app.session.logout()

def test_modify_email(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(email="gilmirahman@gmail.com"))
    app.session.logout()

def test_modify_address2(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(address2="Ekaterinburg, Selkorovskaya, 2 apt 56"))
    app.session.logout()