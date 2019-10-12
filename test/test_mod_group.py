__author__ = 'Liliia'

from model.group import Group
import random
import allure

def test_modify_group_name(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
        new_group = Group(name="edited group")
    with allure.step('When I modify a group %s from the list' % group):
        app.group.modify_group_by_id(group.id, new_group)
    with allure.step('Then the new list is equal to the old list with the modified group'):
        new_groups = db.get_group_list()
        for i in old_groups:
            if i.id == group.id:
                i.name = new_group.name
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
