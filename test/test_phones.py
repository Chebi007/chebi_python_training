from random import randrange

def test_phones_on_home_page(app, db):
    phones_from_home_page = app.contact.get_phones_list()
    phones_from_db = db.get_phone_list()
    assert sorted(phones_from_home_page) == sorted(phones_from_db)

def test_phones_on_contact_view_page(app):
    index = randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
