from peewee import *

database = MySQLDatabase('test_1', **{'password': 'Warsong0722', 'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Record(BaseModel):
    address = CharField(db_column='Address', null=True)
    birthday = IntegerField(db_column='Birthday', null=True)
    country = CharField(db_column='Country', null=True)
    ctfid = CharField(db_column='CtfId', null=True)
    ctftype = CharField(db_column='CtfType', null=True)
    email = CharField(db_column='Email', null=True)
    gender = CharField(db_column='Gender', null=True)
    mobile = CharField(db_column='Mobile', null=True)
    name = CharField(db_column='Name', null=True)
    zip = CharField(db_column='Zip', null=True)

    class Meta:
        db_table = 'records'

