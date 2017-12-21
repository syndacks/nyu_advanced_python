import datetime as dt

class Guestbook(object):
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

    def print_entries(self):
        """loop through entries and print each entry's info"""
        print "Entries for |-" + self.title + "-| (id: " + self.id + "): "
        for entry in self.entries:
            print '- {} said {} on {}'.format(entry.author, entry.comment, entry.timestamp)


class Entry(object):
    def __init__(self, author, comment, timestamp=None):
        self.author = author
        self.comment = comment
        self.timestamp = dt.datetime.now()
