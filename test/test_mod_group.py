__author__ = 'Liliia'

from model.group import Group

def test_modify_first_name(app):
    app.group.modify_first(Group(name="edited group"))

def test_modify_first_header(app):
    app.group.modify_first(Group(header="edited group"))

def test_modify_first_footer(app):
    app.group.modify_first(Group(footer="edited group"))