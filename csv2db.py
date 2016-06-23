# coding: utf-8
import csv
import CSVlist
from mysqldb import MySQL
from dbconfig import db_config

def proc(addr, db, drop_headline=False):
    file_handler = csv.reader(open(addr, 'rb'))
    if drop_headline:
        file_handler.next()
    tmp = []
    counter = 1
    for item in file_handler:
        if counter > 4500:
            print len(tmp)
            db.insert_many(tmp)
            # reset
            tmp = []
            counter = 1
        item = tuple([item[k] for k in (0,3,4,5,6,7,8,11,19,22)])
        tmp.append(item)
        counter += 1
    db.close()

def proc_many(queue, db, drop_headline=False):
    for addr in queue:
        proc(addr, db, drop_headline)

if __name__ == "__main__":
    store = MySQL(db_config)
    queue = CSVlist.namelist()
    proc_many(queue, store, True)
    print 'end without exception'
