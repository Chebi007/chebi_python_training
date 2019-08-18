
from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina", lastname="Marinina"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(2, len(old_contacts)+2)
    contact = Contact(firstname="Lesya", lastname="Lavrova")
    contact.id = old_contacts[index-2].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index-2] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Marina"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first(Contact(middlename="Uralovna modified"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)