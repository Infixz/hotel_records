"""model set"""
# coding: utf
import torndb
import MySQLdb
import peewee


class tnlocal_mysql:
    def __init__(self,db_name,user=None,passwd=None):
        self.db = torndb.Connection("localhost:3306",db_name,user=user,password=passwd)

tndb = tnlocal_mysql('hotel_buiz','root','Warsong0722')

pw_local_mysql = peewee.MySQLDatabase(
    'hotel_buiz',
    user='root',
    password='Warsong0722',
    host='localhost',
    port=3306
)

class pwHotelRecord(peewee.Model):
    id = peewee.IntegerField(
        
        primary_key=True
    )
    Name = peewee.CharField(
        max_length=255
    )
    CtfType = peewee.CharField(
        max_length=255
    )
    CtfId = peewee.CharField(
        max_length=255
    )
    Gender = peewee.CharField(
        max_length=255
    )
    Birthday = peewee.IntegerField(
        
    )
    Address = peewee.CharField(
        max_length=300
    )
    Zip = peewee.CharField(
        max_length=8
    )
    Country = peewee.CharField(
        max_length=10
    )
    Mobile = peewee.CharField(
        max_length=30
    )
    Email = peewee.CharField(
        max_length=50
    )

    class Meta:
        database = pw_local_mysql
        db_table = 'records'

        
