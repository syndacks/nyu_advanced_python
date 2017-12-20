import sqlite3
import datetime as dt
import uuid
from active_relational_record import ActiveRelationalRecord

class Guestbook(ActiveRelationalRecord):
    def __init__(self, title=None):
        self.id = str(uuid.uuid4())
        self.title = title

    def entries(self):
        query = {'guestbook_id': self.id}
        return self.get_row('Entry',**query)

class Entry(ActiveRelationalRecord):
    def __init__(self, guestbook_id, author, content):
        self.id = str(uuid.uuid4())
        self.guestbook_id = guestbook_id
        self.author = author
        self.content = content
        self.timestamp = dt.datetime.now()

    def guestbook(self):
        query = {'id': self.guestbook_id}
        return self.get_row('Guestbook',**query)

if __name__ == '__main__':
    # create an instance of guestbook
    guestbook = Guestbook.create(title="hello world")
    # update that instance
    guestbook.update(title="new title")
    # create an entry belonging to a guestbook
    entry1 = Entry.create(guestbook_id=guestbook.id, author='Cyrus', content='this is my first entry')
    # update that entry
    entry1.update(author='David', content='new content')

    #get the guestbook for which the entry belongs to
    entry1.guestbook()

    # find a particular entry
    Entry.find_by(id=entry1.id)
    Entry.create(guestbook_id=guestbook.id, author='David', content='lalallalalal')
    Entry.create(guestbook_id=guestbook.id, author='Roger', content='ththhatalal')
    #get all entries associated with a particular guestbook
    print(guestbook.entries())
