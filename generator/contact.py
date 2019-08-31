from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return (prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])).replace("'", "").\
        replace("\\", "").replace("<", "").replace('"', "").replace("  ", " ").replace("   ", " ")

testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="", secondaryphone="")] + [
    Contact(firstname=random_string("firstname:", 20), middlename=random_string("middlename:", 20),
            lastname=random_string("lastname:", 20), nickname=random_string("nickname:", 20),
            title=random_string("title:", 20), company=random_string("company:", 20),
            address1=random_string("adress1:", 30), homephone=random_string("H:", 20),
            mobilephone=random_string("M:", 20), workphone=random_string("W:", 20), secondaryphone=random_string("P:", 20),
            email=random_string("email:", 20), email2=random_string("email2:", 20), email3=random_string("email3:", 20),
            address2=random_string("adress2:", 30))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))