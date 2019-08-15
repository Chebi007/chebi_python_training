
from model.contact import Contact

def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(firstname="Marina modified"))

def test_modify_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(middlename="Uralovna modified"))

def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(lastname="Kuzyeva edited"))

def test_modify_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(nickname="chebi modified"))

def test_modify_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(title="Tester modified"))

def test_modify_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(company="Bank modified"))

def test_modify_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(address="Ekaterinburg, Surikova 60, apt 12"))

def test_modify_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(mobile="+79505471137"))

def test_modify_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(email="gilmirahman@gmail.com"))

def test_modify_address2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    app.contact.modify_first(Contact(address2="Ekaterinburg, Selkorovskaya, 2 apt 56"))