
from model.contact import Contact

def test_modify_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(firstname="Liliia modified", middlename="Uralovna modified", lastname="Kuzyeva edited", nickname="chebi modified", title="Tester modified", company="Bank modified", address="Ekaterinburg, Surikova 60, apt 12", mobile="+79505471137", email="gilmirahman@gmail.com", address2="Ekaterinburg, Selkorovskaya, 2 apt 56"))
    app.session.logout()