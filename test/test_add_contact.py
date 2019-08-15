# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Liliia", middlename="Uralovna", lastname="Kuzyeva", nickname="chebi", title="Tester", company="Bank", address="Ekaterinburg, Surikova 60, apt 12", mobile="+79505471137", email="gilmirahman@gmail.com", address2="Ekaterinburg, Selkorovskaya, 2 apt 56"))
