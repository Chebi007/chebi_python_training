
from model.contact import Contact
import random
import allure

def test_modify_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="Marina", lastname="Marinina"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
        new_contact = Contact(firstname="Kristina", lastname="Lavrova")
    with allure.step('When I modify a contact %s from the list' % contact):
        app.contact.modify_contact_by_id(contact.id, new_contact)
    with allure.step('Then the new list is equal to the old list with modified contact'):
        new_contacts = db.get_contact_list()
        for i in old_contacts:
            if i.id == contact.id:
                i.firstname = new_contact.firstname
                i.lastname = new_contact.lastname
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
