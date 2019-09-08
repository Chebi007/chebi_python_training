

def test_address1_on_home_page(app, db):
    addresses_from_home_page = app.contact.get_address_list()
    addresses_from_db = db.get_address_list()
    assert sorted(addresses_from_home_page) == sorted(addresses_from_db)
