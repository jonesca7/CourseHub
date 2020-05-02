from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Course
import json

app = Flask(__name__)

# app.config["MONGODB_SETTINGS"] = {
#     "host" : "mongodb://localhost/course-hub"
# }

app.config['MONGODB_SETTINGS'] = {
    "db": "course-hub",
    'host': 'mongodb://localhost:27017/course-hub'
}

initialize_db(app)


# { "name" : "Test Course A",
#   "topic" : "Web Development",
#   "platform" : "Coursera",
#   "url" : "https://www.coursera.org/learn/mindshift"
# }


# The Home page is accessible to anyone
@app.route('/')
def home_page():
    # String-based templates
    return {"hello" : "world"}

@app.route("/courses")
def get_courses():
    courses = Course.objects().to_json()
    return Response(courses, mimetype="application/json", status=200)


@app.route("/courses", methods=["POST"])
def add_course():
    body = request.get_json(force=True)
    course = Course(**body).save()
    id = course.id
    return {"id" : str(id)}, 200


@app.route("/courses/<id>")
def get_course(id):
    courses = Course.objects.get(id=id).to_json()
    return Response(courses, mimetype="application/json", status=200)


@app.route("/courses/<id>", methods=["PUT"])
def update_course(id):
    body = request.get_json(force=True)
    Course.objects.get(id=id).update(**body)
    return "", 200


@app.route("/courses/<id>", methods=["DELETE"])
def delete_course(id):
    course = Course.objects.get(id=id).delete()
    return "None", 200


if __name__ == "__main__":
    app.run()

# Download Postman from https://www.postman.com/ to test API
# Tutorial series: https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650

# Installing Flask and Mongo requirements on your machine
# sudo -H pip install -U pipenv
# pipenv install flask
# pipenv install flask-mongoengine

# Type below in terminal to run the app
# mongod (to start db server)
# Type following in a new terminal window
# pipenv shell
# python3 app.py