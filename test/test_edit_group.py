__author__ = 'Liliia'

from model.group import Group

def test_edit_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited group", header="edited group", footer="edited group"))
    app.session.logout()