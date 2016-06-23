# coding:utf-8
import MySQLdb

class mysqldb:
    def __ini__(self,user,passwd,db):
        self.db = MySQLdb.connect(user,passwd,db)
        self.cursor = self.db.cursor()
    def save_many(tuple_tar):
        self.cursor.executemany(
        """insert into records (Name, CtfType, CtfId, Gender, Birthday, Address, Zip, Country, Mobile, Email) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",tuple_tar)
        self.cursor.commit()
    def close():
        self.cursor.close()
        self.db.close()
