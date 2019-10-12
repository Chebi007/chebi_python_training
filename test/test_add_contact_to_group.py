from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
import string
import allure

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


new_contact = Contact(firstname=random_string("firstname:", 20), middlename=random_string("middlename:", 20),
            lastname=random_string("lastname:", 20))
new_group = Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))


def test_add_contact_to_group(app):
    with allure.step('Given a non-empty list of contacts'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(new_contact)
    with allure.step('Given a non-empty list of groups'):
        if len(db.get_group_list()) == 0:
            app.group.create(new_group)
    with allure.step('Given a contact not in all groups'):
        for contact in db.get_contact_list():
            if len(db.get_group_list()) != len(db.get_group_list_for_contact(contact)):
                contact = contact
                break
        else:
            app.contact.create(new_contact)
            contact = db.get_contact_list()[-1]
    with allure.step('Given a random group from the list of groups the contact does not belong'):
        groups = db.get_group_list()
        groups_for_contact = db.get_group_list_for_contact(contact)
        groups_for_contact_free = [group for group in groups if group not in groups_for_contact]
        group = random.choice(groups_for_contact_free)
    with allure.step('When I add contact %s to the random group %s' % (contact, group)):
        app.contact.add_contact_to_group(contact, group)
    with allure.step('Then the contact %s is in the group %s' % (contact, group)):
        assert contact in db.get_contacts_in_group(Group(id=group.id))