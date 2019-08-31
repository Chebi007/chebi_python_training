__author__ = 'Liliia'

from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="edited group")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    for i in old_groups:
        if i.id == group.id:
            i.name = new_group.name
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
