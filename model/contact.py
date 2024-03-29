__author__ = 'Liliia'

from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, fullname=None, nickname=None, title=None,
                 company=None, address1=None, id=None, homephone=None, mobilephone=None, workphone=None,
                 secondaryphone=None, all_phones_from_home_page=None, email=None, email2=None, email3=None,
                 all_emails_from_home_page=None, all_emails_on_view_page=None, address2=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.fullname = fullname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address1 = address1
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_emails_on_view_page = all_emails_on_view_page
        self.address2 = address2
        self.id = id

    def __repr__(self):
        return "\"%s %s\"" % (self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize