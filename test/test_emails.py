from random import randrange

def test_emails_on_home_page(app, db):
    email_from_home_page = app.contact.get_email_list()
    email_from_db = db.get_email_list()
    assert sorted(email_from_home_page) == sorted(email_from_db)

def test_emails_on_contact_view_page(app):
    index = randrange(app.contact.count())
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    assert contact_from_view_page.all_emails_on_view_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)


