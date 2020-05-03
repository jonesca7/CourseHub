from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Course(db.Document):
    name = db.StringField(required=True, unique=True)
    topic = db.StringField(required=True, unique=True)
    platform = db.StringField(required=True, unique=True)
    url = db.StringField(required=True, unique=True)
    added_by = db.ReferenceField("User")
    

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    courses = db.ListField(db.ReferenceField("Course", reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Course, "added_by", db.CASCADE)