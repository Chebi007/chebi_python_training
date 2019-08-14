__author__ = 'Liliia'

from model.group import Group

def test_modify_first_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="edited group"))
    app.session.logout()

def test_modify_first_header(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(header="edited group"))
    app.session.logout()

def test_modify_first_footer(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(footer="edited group"))
    app.session.logout()