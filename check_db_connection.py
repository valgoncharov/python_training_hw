from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
   l = db.get_contacts_not_in_group(Group(id="11")) #get_group_list #get_contact_list #get_contacts_in_group
   for item in l:
       print(item)
   print(len(l))
finally:
    pass #db.destroy()
