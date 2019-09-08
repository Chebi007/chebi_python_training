from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Marina", lastname="Marinina"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group(contact, group)
    contacts_in_group = [i for i in db.get_contact_list() if i not in db.get_contacts_not_in_group(Group(id=group.id))]
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(db.get_contacts_in_group(Group(id=group.id)), key=Contact.id_or_max)


