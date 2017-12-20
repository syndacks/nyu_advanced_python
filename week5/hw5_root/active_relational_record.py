import sqlite3
from db_manager import DbManager

class ActiveRelationalRecord(object):
    @classmethod
    def create(cls,**kwargs):
        obj = cls(**kwargs)
        obj.exec_create(obj.__dict__)
        return obj

    @classmethod
    def find_by(cls, **kwargs):
        db_connection = DbManager()
        return db_connection.retrieve(cls.__name__, **kwargs)

    @classmethod
    def find_all(cls):
        db_connection = DbManager()
        return db_connection.retrieve_all(cls.__name__)

    def update(self, **kwargs):
        self.set_attr(**kwargs)
        self.exec_update(self.__dict__)
        return self

    def set_attr(self, **kwargs):
        self.__dict__.update(kwargs)
        return self

    def exec_update(self, fields):
        db_connection = DbManager()
        db_connection.update(type(self).__name__, self.id, fields)
        print(db_connection.retrieve(type(self).__name__, **fields))
        return

    def exec_create(self, fields):
        db_connection = DbManager()
        db_connection.insert(type(self).__name__, fields)
        print(db_connection.retrieve(type(self).__name__, **fields))
        return

    def get_row(self, table_name, **kwargs):
        db_connection = DbManager()
        return db_connection.retrieve(table_name, **kwargs)
