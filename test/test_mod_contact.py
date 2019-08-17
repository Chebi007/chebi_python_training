
from model.contact import Contact

def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Marina"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Lesya")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Marina"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first(Contact(middlename="Uralovna modified"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)