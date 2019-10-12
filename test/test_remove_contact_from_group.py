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


def test_remove_contact_from_group(app):
    with allure.step('Given a non-empty list of contacts'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(new_contact)
    with allure.step('Given a non-empty list of groups'):
        if len(db.get_group_list()) == 0:
            app.group.create(new_group)
    with allure.step('Given a group with the list of contacts'):
        for group in db.get_group_list():
            if len(db.get_contacts_not_in_group(group)) != 0:
                group = group
                break
        else:
            app.group.create(new_group)
            group = db.get_group_list()[-1]
    with allure.step('Given a random contact from the list of contacts not in group %s' % group):
        contacts_not_in_group = db.get_contacts_not_in_group(group)
        contact = random.choice(contacts_not_in_group)
    with allure.step('When I delete contact from the group %s' % group):
        app.contact.add_contact_to_group(contact, group)
        app.contact.remove_contact_from_group(contact, group)
    with allure.step('Then the contact %s not in list of contacts for group %s' % (contact, group)):
        assert contact not in db.get_contacts_in_group(group)
