import mongoengine.fields
from mongoengine import*

connect('pupils')

class school(Document):
    School_Nun = mongoengine.fields.IntField(max_length=1000, required=True)
    School_Name = StringField(max_length=20, required=True)

class User(Document):
    School_N = mongoengine.fields.IntField(max_length=1000, required=True)
    Class_N = StringField(max_length=20, required=True)
    first_name = StringField(max_length=20, required=True)
    last_name = StringField(max_length=20, required=True)

class classes(Document):
    clas = StringField(max_length=20, required=True)


