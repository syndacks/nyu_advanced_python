import sqlite3

class DbManager(object):
    db = 'data/mydb'
    def __init__(self, dblocation=db):
        self.conn = sqlite3.connect(dblocation)
        self.cur = self.conn.cursor()
        self.create_table_guest()
        self.create_table_entry()

    def insert(self, table_name, args):
        query = 'INSERT INTO ' + table_name + ' (' + ','.join(args.keys()) + ') VALUES (' + ','.join(['?'] * len(args.keys()))+ ')'
        print('\033[31m' + query + '\033[0m')
        self.cur.execute(query, args.values())
        self.conn.commit()

    def update(self, table_name, uid, args):
        query = "UPDATE {} SET {} WHERE id = ?".format(table_name, ", ".join('{} = "{}"'.format(k, args[k]) for k in args), uid)
        print('\033[31m' + query + '\033[0m')
        self.cur.execute(query,(uid,))
        self.conn.commit()

    def retrieve(self, table_name, **args):
        query = "SELECT * FROM {} WHERE {}".format(table_name, " AND ".join('{} = "{}"'.format(k, args[k]) for k in args))
        print('\033[31m' + query + '\033[0m')
        self.cur.execute(query)
        return self.cur.fetchall()

    def retrieve_all(self, table_name):
        query = "SELECT * FROM {}".format(table_name)
        print('\033[31m' + query + '\033[0m')
        self.cur.execute(query)
        return self.cur.fetchall()

# TODO: find something better for these two methods (it sucks)
    def create_table_guest(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Guestbook (id TEXT, title TEXT)''')
        self.conn.commit()

    def create_table_entry(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Entry (id TEXT, guestbook_id TEXT, author TEXT, content TEXT, timestamp DATE)''')
        self.conn.commit()

    def __del__(self):
        '''call destructor when object is GC'''
        self.conn.close()
