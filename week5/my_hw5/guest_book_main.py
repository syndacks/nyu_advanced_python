import uuid
import datetime as dt

class Guestbook(object):
    """if this Guestbook is new (i.e., if the id can't be found in the \n
     datastore),a new Guestbook is created and will be stored; if it is not \n
    new, it is retrieved from the datastore below)"""

    def __init__(self, id, title=None, entries=None):
        self.id = id
        self.title = title
        self.entries = []

    def add_entry(self, entry_object):
        """given Entry object, add object to the Guestbook's internal list of \n
        entries"""
        self.entries.append(entry_object)

    def set_title(self, title):
        """allows for the resetting of the Guestbook title"""
        self.title = title


class Entry(object):
    """ """
    def __init__(self, author, comment, timestamp=None):
        self.author = author
        self.comment = comment
        self.timestamp = dt.datetime.now().microsecond


def store_guestbook(guestbook_object):
    """store the object"""

def retrieve_guestbook(guestbook_id):
    """retrieve the object"""


# guestbook_id = '1'
# guestbook_title = 'My Guestbook'
# guestbook = Guestbook(guestbook_id, guestbook_title) # retrieves existing Guestbook from datastore, or creates new
# print guestbook.__dict__
# guestbook.set_title('Dacks Guestbooks')
# print guestbook.__dict__

entry = Entry('David', 'I like it!') # populates Entry object attrs: .name, .comment, .timestamp
print entry.__dict__


# guestbook.add_entry(entry) # adds Entry object to internal list in its .entries attribute
#
# guestbook.add_entry(Entry('George', "I dont'")
