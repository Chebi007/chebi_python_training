# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import string
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return (prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])).replace("'", "").replace("\\", "").replace("<", "").replace('"', "")


testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="", secondaryphone="")] + [
    Contact(firstname=random_string("firstname:", 20), middlename=random_string("middlename:", 20),
            lastname=random_string("lastname:", 20), nickname=random_string("nickname:", 20),
            title=random_string("title:", 20), company=random_string("company:", 20),
            address1=random_string("adress1:", 30), homephone=random_string("H:", 20),
            mobilephone=random_string("M:", 20), workphone=random_string("W:", 20), secondaryphone=random_string("P:", 20),
            email=random_string("email:", 20), email2=random_string("email2:", 20), email3=random_string("email3:", 20),
            address2=random_string("adress2:", 30))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)