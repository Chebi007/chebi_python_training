from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
import string

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


new_contact = Contact(firstname=random_string("firstname:", 20), middlename=random_string("middlename:", 20),
            lastname=random_string("lastname:", 20))
new_group = Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))


def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(new_contact)
    if len(db.get_group_list()) == 0:
        app.group.create(new_group)
    for contact in db.get_contact_list():
        if len(db.get_group_list()) != len(db.get_group_list_for_contact(contact)):
            contact = contact
            break
    else:
        app.contact.create(new_contact)
        contact = db.get_contact_list()[-1]
    groups = db.get_group_list()
    groups_for_contact = db.get_group_list_for_contact(contact)
    groups_for_contact_free = [group for group in groups if group not in groups_for_contact]
    group = random.choice(groups_for_contact_free)
    app.contact.add_contact_to_group(contact, group)
    assert contact in db.get_contacts_in_group(Group(id=group.id))