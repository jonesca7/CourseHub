from .db import db

class Course(db.Document):
    name = db.StringField(required=True, unique=True)
    topic = db.StringField(required=True, unique=True)
    platform = db.StringField(required=True, unique=True)
    url = db.StringField(required=True, unique=True)
    
    # if we need to store lists
    # casts = db.ListField(db.StringField(), required=True)
    # genres = db.ListField(db.StringField(), required=True)