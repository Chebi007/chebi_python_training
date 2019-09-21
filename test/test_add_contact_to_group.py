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
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contacts_not_in_group(Group(id=group.id)))
    app.contact.add_contact_to_group(contact, group)
    assert contact not in db.get_contacts_not_in_group(Group(id=group.id))



