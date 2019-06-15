__author__ = 'Liliia'

from model.group import Group

def test_modify_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="edited group", header="edited group", footer="edited group"))
    app.session.logout()