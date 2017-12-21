import pickle
from pprint import pprint
from guestbook_classes import Entry, Guestbook

def store_guestbook(guestbook_object):
    """store the guestbook object in a pickle file"""
    wfh = open('gbfile.pickle', 'wb')
    pickle.dump(guestbook_object, wfh)
    print guestbook_object.title + " has been saved."

def retrieve_guestbook(guestbook_id):
    """retrieve the guestbook_id"""
    fh = open('gbfile.pickle', 'rb')
    guestbook = pickle.load(fh)
    return guestbook

if __name__ == '__main__':
    # create guestbook id and title variables
    guestbook_id = 'a8b1'
    guestbook_title = 'Dacks Guestbook'
    # instantiate a guestbook with above variables
    guestbook = Guestbook(guestbook_id, guestbook_title)

    # create some entries of guests and their comments
    entry1 = Entry('Steve', 'It was pretty good.')
    entry2 = Entry('Dacks', 'I fuckin hated it!')
    entry3 = Entry('Veronica', 'The tacos were great!!')
    # store the entries in the guestbook
    entries = [entry1, entry2, entry3]
    for entry in entries:
        guestbook.add_entry(entry)

    # print out the entries by looping over guestbook.entries
    guestbook.print_entries()

    # persist data via store_guestbook (Pickle)
    store_guestbook(guestbook)

    # we can load the guestbook and add more to it
    print "--------------loaded------------------"
    loaded_guestbook = retrieve_guestbook(guestbook)
    entry4 = Entry('Joe', 'Where\'s the nearest bar?')
    loaded_guestbook.add_entry(entry4)
    loaded_guestbook.print_entries()
    store_guestbook(loaded_guestbook)
