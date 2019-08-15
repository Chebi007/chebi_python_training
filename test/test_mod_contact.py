
from model.contact import Contact

def test_modify_firstname(app):
    app.contact.modify_first(Contact(firstname="Liliia modified"))

def test_modify_middlename(app):
    app.contact.modify_first(Contact(middlename="Uralovna modified"))

def test_modify_lastname(app):
    app.contact.modify_first(Contact(lastname="Kuzyeva edited"))

def test_modify_nickname(app):
    app.contact.modify_first(Contact(nickname="chebi modified"))

def test_modify_title(app):
    app.contact.modify_first(Contact(title="Tester modified"))

def test_modify_company(app):
    app.contact.modify_first(Contact(company="Bank modified"))

def test_modify_address(app):
    app.contact.modify_first(Contact(address="Ekaterinburg, Surikova 60, apt 12"))

def test_modify_mobile(app):
    app.contact.modify_first(Contact(mobile="+79505471137"))

def test_modify_email(app):
    app.contact.modify_first(Contact(email="gilmirahman@gmail.com"))

def test_modify_address2(app):
    app.contact.modify_first(Contact(address2="Ekaterinburg, Selkorovskaya, 2 apt 56"))