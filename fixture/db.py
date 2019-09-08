import pymysql.cursors
from model.group import Group
from model.contact import Contact
from fixture.contact import ContactHelper
import re

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname.strip(), lastname=lastname.strip()))
        finally:
            cursor.close()
        return list

    def get_address_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select address from addressbook where deprecated='0000-00-00 00:00:00'")
            for address in cursor:
                list.append(address[0])
        finally:
            cursor.close()
        return list

    def get_email_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (email, email2, email3) = row
                list.append("\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                           [email.strip(), email2.strip(), email3.strip()]))))
        finally:
            cursor.close()
        return list


    def clear(self, s):
        return re.sub("[- (\)./]", "", s)

    def get_phone_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select home, mobile, work , phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (home, mobile, work, phone2) = row
                list.append("\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                                           [home.strip(), mobile.strip(), work.strip(), phone2.strip()])))))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()