from mongoengine import Document,StringField,ListField

class Infomation(Document):
    FirstName = StringField()
    LastName = StringField()
    Email = StringField()
    Yob = StringField()
    Gender = StringField()
    City = StringField()
    code = StringField()