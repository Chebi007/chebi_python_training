__author__ = 'Liliia'

from model.group import Group

def test_modify_first_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(name="edited group"))

def test_modify_first_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(header="edited header"))

def test_modify_first_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(footer="edited footer"))