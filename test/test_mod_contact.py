
from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Marina", lastname="Marinina"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="Kristina", lastname="Lavrova")
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    for i in old_contacts:
        if i.id == contact.id:
            i.firstname = new_contact.firstname
            i.lastname = new_contact.lastname
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
