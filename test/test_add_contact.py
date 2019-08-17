# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Liliia", middlename="Uralovna", lastname="Kuzyeva", nickname="chebi", title="Tester", company="Bank", address="Ekaterinburg, Surikova 60, apt 12", mobile="+79505471137", email="gilmirahman@gmail.com", address2="Ekaterinburg, Selkorovskaya, 2 apt 56")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)